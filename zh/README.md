# AI工程师面试全攻略 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](../CONTRIBUTING.md)

> 精选的AI/ML工程师面试准备资源合集 — 涵盖LLM系统设计、GenAI基础、行为面试、薪资基准和公司专属指南。

[English Version](../README.md)

---

## 目录

- [学习计划](#学习计划)
- [LLM基础与GenAI](#llm基础与genai)
- [ML系统设计](#ml系统设计)
- [经典ML与统计](#经典ml与统计)
- [AI岗位编程](#ai岗位编程)
- [AI岗位行为面试](#ai岗位行为面试)
- [薪资与待遇](#薪资与待遇)
- [公司面试指南](#公司面试指南)
- [真实面经](#真实面经)
- [LLM评估与测试](#llm评估与测试)
- [AI安全与伦理](#ai安全与伦理)
- [工具与框架](#工具与框架)
- [书籍与课程](#书籍与课程)
- [社区与论坛](#社区与论坛)

---

## 学习计划

### 30天冲刺计划（在职跳槽）

| 周 | 重点 | 每日时间 | 核心任务 |
|----|------|---------|---------|
| 1 | 基础 | 3-4小时 | ML基础复习、Transformer架构深入、每天2道LeetCode |
| 2 | 系统设计 | 3-4小时 | 每天1个ML系统设计案例、RAG/Agent架构模式 |
| 3 | 行为+公司 | 2-3小时 | 准备AI场景STAR故事、目标公司研究、模拟面试 |
| 4 | 模拟+打磨 | 2-3小时 | 每天2场模拟面试、弱项复习、Offer谈判准备 |

### 60天均衡计划（在职准备）

| 阶段 | 周数 | 重点 | 每日时间 |
|------|------|------|---------|
| 夯基 | 1-3 | ML/DL基础、LLM内部原理、编程模式 | 1.5-2小时 |
| 应用 | 4-6 | 系统设计案例、行为面试准备、简历优化 | 1.5-2小时 |
| 冲刺 | 7-8 | 模拟面试、公司定向准备、谈判练习 | 2小时 |

---

## LLM基础与GenAI

### 面试高频题

| # | 问题 | 难度 | 时间 |
|---|------|------|------|
| 1 | 解释Self-Attention机制。计算复杂度是什么？Flash Attention如何优化？ | 中等 | 15分钟 |
| 2 | 对比RLHF、DPO和GRPO的对齐方法。什么场景选哪个？ | 困难 | 20分钟 |
| 3 | 需要以<200ms P95延迟服务70B参数模型，说说你的优化策略。 | 困难 | 30分钟 |
| 4 | 设计一个法律文档搜索的RAG流水线。如何处理分块、向量模型选择和混合检索？ | 困难 | 30分钟 |
| 5 | Fine-tuning和In-context learning的权衡是什么？各适合什么场景？ | 中等 | 15分钟 |
| 6 | LoRA的原理是什么？为什么能减少显存？和全量微调相比有什么局限？ | 中等 | 15分钟 |
| 7 | 如何在生产环境中检测和缓解LLM幻觉？ | 中等 | 20分钟 |
| 8 | 对比主流Embedding模型（OpenAI ada-002、Cohere embed-v3、BGE、E5），如何评估选择？ | 中等 | 15分钟 |
| 9 | AI Agent和AI Pipeline的区别是什么？什么时候用确定性工作流vs Agent循环？ | 中等 | 15分钟 |
| 10 | 你在做一个客服聊天机器人，LLM有时会泄露内部定价和策略。如何实现防护栏？ | 困难 | 25分钟 |

---

## AI岗位行为面试

### AI场景行为面试题

| # | 问题 | 框架 | 难度 |
|---|------|------|------|
| 1 | 说说你的模型在生产环境出问题的经历。发生了什么？你做了什么改变？ | STAR + 根因分析 | 中等 |
| 2 | 描述一个你和研究员在模型架构上有分歧的场景。你是怎么解决的？ | STAR + 冲突解决 | 中等 |
| 3 | 你上线了一个LLM功能，但用户投诉幻觉严重。你的应对流程是什么？ | STAR + 事故响应 | 困难 |
| 4 | 说说你把一个复杂ML概念解释给非技术利益相关者的经历。 | STAR + 沟通 | 简单 |
| 5 | 描述一个你需要在模型准确率和服务成本/延迟之间做取舍的项目。 | STAR + 权衡 | 中等 |

---

## 薪资与待遇

### AI/ML工程师薪资（2025-2026美国市场）

| 公司 | 级别 | 岗位 | 基本工资 | 股票(年) | 奖金 | 总包 |
|------|------|------|---------|---------|------|------|
| Google | L4 | MLE | $160-185K | $80-120K | 15% | $280-380K |
| Google | L5 | MLE | $195-230K | $150-250K | 15% | $400-550K |
| Meta | E4 | MLE | $165-190K | $80-130K | 10% | $280-390K |
| Meta | E5 | MLE | $200-240K | $150-300K | 15% | $410-620K |
| OpenAI | L3 | RE | $200-250K | PPUs | — | $350-600K+ |
| Anthropic | Mid | RE | $200-260K | equity | — | $350-550K |
| NVIDIA | Mid | MLE | $160-200K | $80-140K | 10% | $280-400K |

*数据来源：[levels.fyi](https://levels.fyi)、Blind、公开H1B记录*

---

## 公司面试指南

### Anthropic

**面试流程：** 招聘人员电话 → 技术电话面试（编程+ML）→ 现场面试（4-5轮：编程、ML深度、系统设计、研究讨论、价值观/行为）

**核心考察：** AI安全和对齐研究的深刻理解。扎实的编程+ML基础。对构建安全、有益AI系统的热情。

**重点话题：** Constitutional AI、RLHF/DPO、红队测试、可解释性、Scaling Laws、评估方法论。

### OpenAI

**面试流程：** 招聘人员电话 → 技术筛选（编程）→ 现场面试（4-6轮：编程、ML/AI深度、系统设计、过往项目深入、行为）

**核心考察：** 扎实的工程基础+深厚的AI/ML知识。在模糊问题上工作的能力。AI产品交付或研究发表记录。

### Google DeepMind

**面试流程：** 招聘人员电话 → 电话面试（2轮：编程+ML）→ 现场面试（5轮：2轮编程、ML广度、ML深度/系统设计、Googleyness/领导力）

**核心考察：** 扎实的算法基础（L5+需要系统设计）。至少一个领域的研究深度（NLP、CV、RL、优化）。

---

## 社区与论坛

### 英文社区
- [r/MachineLearning](https://www.reddit.com/r/MachineLearning/) - Reddit的ML研究社区
- [r/cscareerquestions](https://www.reddit.com/r/cscareerquestions/) - 求职讨论和面试经验
- [Blind](https://www.teamblind.com) - 匿名职场论坛，验证员工身份
- [Hugging Face Discord](https://huggingface.co/join/discord) - 开源AI社区

### 中文社区
- [知乎 ML话题](https://www.zhihu.com/topic/19559450) - ML职业和面试讨论
- [掘金](https://juejin.cn/) - 中文开发者社区，AI/ML内容丰富
- [Datawhale](https://github.com/datawhalechina) - 中国最大的AI学习者社区
- [V2EX](https://www.v2ex.com/) - 开发者社区，技术讨论
- [牛客网](https://www.nowcoder.com/) - 面经分享和在线笔试练习

---

## 许可证

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

本作品使用 [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) 许可。
