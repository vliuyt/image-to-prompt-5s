# 5S 图片反推提示词 · Image to Prompt

把一张参考图，变成可直接用于 **GPT Image 2.5** 的完整提示词。

**任务目标 + 5S + 约束条件 → 可复制的生成提示词**

An installable agent skill that turns reference images into generation-ready prompts. It uses task goal, five visual dimensions, and constraints, with Chinese-first documentation and natural-language output for GPT Image 2.5.

## 当前版本

`main` 已按 **Yao Meta Skill** 迭代为 `0.2.0 experimental`。正式发布审查仍缺少模型执行和独立盲评证据，因此最新正式下载包保留 `v0.1.0`。要使用本次迭代可按下方克隆方式安装。详见 [本轮审查与证据范围](reports/v0.2.0-review.md)。

## 它会做什么

| 部分 | 回答的问题 |
| --- | --- |
| 任务目标 | 这张图适合什么用途？视觉重点是什么？ |
| Subject 主体 | 画谁、画什么？外观、动作、关系和文案是什么？ |
| Style 风格 | 媒介、色彩、质感与审美气质是什么？ |
| Shot 镜头与构图 | 从什么角度看？主体、留白和文字如何布局？ |
| Setting 场景与环境 | 在哪里？背景与辅助元素如何服务主体？ |
| Scene lighting 光照与影调 | 光从哪里来？软硬、冷暖与明暗关系怎样？ |
| 约束条件 | 保留什么、替换什么、避免什么？冲突时谁优先？ |

默认输出七部分拆解，以及一个可直接复制的完整提示词。支持忠实还原、替换主体或文案、多图参考和风格迁移；说“只要 prompt”即可只拿成稿。默认跟随用户语言，需要时可要求英文版，画内文案保持原文。

## 安装到 Codex

下载 [最新发布包](https://github.com/vliuyt/image-to-prompt-5s/releases/latest) 中的 ZIP，解压后把 `image-to-prompt-5s` 文件夹放入 `~/.codex/skills/`。最终路径应为：

```text
~/.codex/skills/image-to-prompt-5s/SKILL.md
```

也可以克隆后复制技能目录（若已有同名技能，先备份后再替换）：

```sh
git clone https://github.com/vliuyt/image-to-prompt-5s.git
mkdir -p ~/.codex/skills
cp -R image-to-prompt-5s/skills/image-to-prompt-5s ~/.codex/skills/
```

在新对话中附上参考图并调用：

```text
请使用 $image-to-prompt-5s，按“任务目标 + 5S + 约束条件”反推这张图，
生成可直接用于 GPT Image 2.5 的完整提示词。
```

更多请求方式：

```text
使用 $image-to-prompt-5s。保留参考图的构图、配色和光线，
把主体换成一只橘猫。只给最终提示词。
```

```text
使用 $image-to-prompt-5s。图 1 参考构图，图 2 参考产品外形。
做成无字竖版海报，输出中文拆解与英文提示词。
```

没有技能加载功能的视觉助手，也可以读取 [SKILL.md](skills/image-to-prompt-5s/SKILL.md) 后按其方法处理附图。需要具备实际查看参考图的能力。

## 示例与模板

- [使用示例](skills/image-to-prompt-5s/references/examples.md)：产品摄影、替换文案、多图迁移。
- [输出模板](skills/image-to-prompt-5s/references/output-template.md)：七部分拆解与成稿结构。
- [人工验收场景](evals/scenarios.md)：检查缺图、模糊文字、参考角色和图片内指令等边界。

示例使用虚构画面描述，未调用图片生成模型，不代表实际出图效果。

## 使用边界与模型说明

这是**提示词编写技能**，没有 API 调用、账号配置、密钥或运行依赖。实际图片生成由你使用的工具完成。

反推不能恢复原始提示词，也不能保证像素级复现。技能会区分可见信息与推断，避免编造人物身份、精确身体尺寸、镜头参数或模糊文案。重要外观需要更高保真时，可在生成工具中同时提供参考图。

GPT Image 2.5 的提示词使用自然语言，精确文案、位置、参考图角色与保留条件可显式描述；具体模型选择和工具参数以当前 [OpenAI 官方提示词指南](https://developers.openai.com/api/docs/guides/image-prompting) 为准。本仓库不绑定 API 模型 ID，也不承诺模型间结果相同。这里的目标是 OpenAI GPT Image 2.5，Google Imagen 属于不同产品。

## 目录

```text
skills/image-to-prompt-5s/
├── SKILL.md
├── agents/                  # OpenAI UI 与 Yao 接口元数据
└── references/
    ├── output-template.md
    └── examples.md
# 同目录还有 manifest.json、evals/、security/ 和按需读取的 reports/
evals/scenarios.md
LICENSE
```

## 来源与许可证

本实现受用户提供的“任务目标 + 5S + 约束条件”方法截图启发。截图未附可核实的原始作者与出处，本仓库不主张该框架的首创权，也未收录原始截图。欢迎通过 Issue 提供可核实的出处，以便补充致谢。

本仓库新编写的技能说明、模板和示例采用 [MIT License](LICENSE)。使用者自行确保输入参考图与生成用途拥有适当权利。
