"""Local harness checks; these mocks are not model execution evidence."""

import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import run_eval as runner


class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.case = {"case_id": "test-case", "user_request": "Describe this image.", "references": []}

    def test_baseline_does_not_receive_snapshot(self):
        self.assertNotIn("SECRET-SNAPSHOT", runner.make_prompt(self.case, "baseline", "SECRET-SNAPSHOT"))

    def test_treatment_receives_exact_frozen_snapshot(self):
        self.assertIn("SECRET-SNAPSHOT", runner.make_prompt(self.case, "with_skill", "SECRET-SNAPSHOT"))

    def test_parent_path_cannot_be_sent_as_fixture(self):
        with self.assertRaises(ValueError):
            runner.safe_fixture("../design.json")

    def run_mock(self, events, returncode=0):
        process = subprocess.CompletedProcess([], returncode, "\n".join(json.dumps(x) for x in events), "")
        with tempfile.TemporaryDirectory() as folder, patch.object(runner.subprocess, "run", return_value=process):
            return runner.run_one(self.case, "baseline", Path(folder), 10, "FROZEN")

    def test_completed_output_requires_observed_usage(self):
        result = self.run_mock([{"type": "item.completed", "item": {"type": "agent_message", "text": "answer"}}])
        self.assertEqual("failed", result["status"])

    def test_prohibited_tool_use_is_not_accepted_as_clean_run(self):
        result = self.run_mock([
            {"type": "item.completed", "item": {"type": "command_execution"}},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "answer"}},
            {"type": "turn.completed", "usage": {"input_tokens": 20, "output_tokens": 3}},
        ])
        self.assertEqual("failed", result["status"])
        self.assertEqual(["command_execution"], result["tool_calls"])

    def test_no_fixture_answer_replay(self):
        case = {**self.case, "fixture_output": "KNOWN-FIXTURE-ANSWER"}
        self.assertNotIn("KNOWN-FIXTURE-ANSWER", runner.make_prompt(case, "baseline", "FROZEN"))

    def test_explicit_failed_turn_cannot_pass_with_output(self):
        result = self.run_mock([
            {"type": "item.completed", "item": {"type": "agent_message", "text": "answer"}},
            {"type": "turn.completed", "usage": {"input_tokens": 20, "output_tokens": 3}},
            {"type": "turn.failed", "error": {"message": "failed"}},
        ])
        self.assertEqual("failed", result["status"])

    def test_top_level_error_cannot_pass(self):
        parsed = runner.parse_events([{"type": "error", "message": "capacity"}])
        self.assertEqual("error", parsed["failure_events"][0]["type"])

    def test_only_confirmed_host_diagnostic_is_tolerated(self):
        known = {"type": "item.completed", "item": {"type": "error", "message": "clamping SessionEnd hook timeout to 3s in private-path"}}
        unknown = {"type": "item.completed", "item": {"type": "error", "message": "unclassified failure"}}
        self.assertTrue(runner.parse_events([known])["host_diagnostics"])
        self.assertFalse(runner.parse_events([known])["failure_events"])
        self.assertTrue(runner.parse_events([unknown])["failure_events"])

    def test_timeout_preserves_partial_private_trace(self):
        timeout = subprocess.TimeoutExpired(["codex"], 10, output=b'{"type":"turn.started"}\n', stderr=b"timeout")
        with tempfile.TemporaryDirectory() as folder, patch.object(runner.subprocess, "run", side_effect=timeout):
            result = runner.run_one(self.case, "baseline", Path(folder), 10, "FROZEN")
            self.assertEqual("failed", result["status"])
            self.assertIn("turn.started", (Path(folder)/"test-case/baseline/events.jsonl").read_text())
            self.assertNotIn("usage", result)


if __name__ == "__main__":
    unittest.main()
