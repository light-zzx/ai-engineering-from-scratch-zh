# My AI Engineering Path
<!-- Managed by the ai-engineering-from-scratch learning skills.
     Repo: https://github.com/fancyboi999/ai-engineering-from-scratch-zh -->

## Mission
硕士二年级学生，学习 AI engineering 是为了以后找实习找工作打基础，顺便为科研打下基础；最好能产出一个扎实的项目丰富简历。课程结束时最想构建什么先不定——先跟课，走完核心课后从 `projects/` 实战层里挑一个做深。

## Placement
- Date: 2026-11-15
- Score: self-selected
- Entry point: Phase 0: 配置与工具
- Pace: ~5 hours/week（工作日约 1 小时，有时不到 1 小时；周末投入较多）
- Note: 自选从阶段 0 起顺序学习。分级测验 10/10，但动手编码基础薄弱、目前依赖 agent 写代码，需要从环境、终端、调试和 Python 基础重新打底。主线优先阶段 0→1→2→3→10→11→13→14→19，其余阶段按岗位方向选修。
- Note: API 课程使用 DeepSeek 官方 API（OpenAI 兼容）替代 Anthropic/OpenAI；鉴权头为 `Authorization: Bearer`。阶段 13 前补 TypeScript 基础（类型、async/await、模块、pnpm），阶段 0–11 的 `.ts` 文件可跳过。

## Path
| Phase | Name | Status | Est. hours |
|-------|------|--------|------------|
| 0 | 配置与工具 | Do | 10 |
| 1 | 数学基础 | Do | 32 |
| 2 | 机器学习基础 | Do | 31 |
| 3 | 深度学习核心 | Do | 19 |
| 4 | 计算机视觉 | Do | 31 |
| 5 | NLP — 从基础到进阶 | Do | 31 |
| 6 | 语音与音频 | Do | 19 |
| 7 | Transformer 深入剖析 | Do | 17 |
| 8 | 生成式 AI | Do | 16 |
| 9 | 强化学习 | Do | 14 |
| 10 | 从零实现 LLM | Do | 33 |
| 11 | LLM 工程 | Do | 21 |
| 12 | 多模态 AI | Do | 67 |
| 13 | 工具与协议 | Do | 76 |
| 14 | 智能体工程 | Do | 57 |
| 15 | 自主系统 | Do | 20 |
| 16 | 多智能体与蜂群 | Do | 31 |
| 17 | 基础设施与生产 | Do | 31 |
| 18 | 伦理、安全与对齐 | Do | 31 |
| 19 | 总结项目 | Do | 627 |

## Progress log
| Date | Lesson | Quiz | Note |
|------|--------|------|------|
| 2026-11-15 | 00/01 开发环境 | self-reported | 本次会话前已完成 |
| 2026-11-15 | 00/02 Git 与协作 | self-reported | 本次会话前已完成 |
| 2026-11-15 | 00/03 GPU 配置与云端 | self-reported | 本次会话前已完成 |
| 2026-11-15 | 00/04 API 与密钥 | 2/3 | 用 DeepSeek 替代 Anthropic；鉴权头误答 x-api-key（应为 Authorization: Bearer）；演示了 os.environ[] 与 .get 的区别；决定阶段 13 前补 TypeScript |

## Review queue
- 00/04 API 与密钥 — 各 provider 的鉴权头差异：`Authorization: Bearer`（DeepSeek/OpenAI 兼容）vs `x-api-key`（Anthropic）
