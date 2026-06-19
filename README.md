# Awesome AI Engineer Interview [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Stars](https://img.shields.io/github/stars/Johnnnmai/awesome-ai-engineer-interview?style=social)](https://github.com/Johnnnmai/awesome-ai-engineer-interview)

> A curated, data-driven, bilingual (EN/中文) field guide to AI engineering roles, interviews, and career growth — covering LLM system design, GenAI fundamentals, behavioral questions, salary benchmarks, company-specific guides, and learning paths.

**[中文版 / Chinese Version](zh/README.md)**

Based on real data: **2,445+ job descriptions**, **51 company interview processes**, real interview experiences, and patterns synthesized from practitioner stories.

**What makes this different from other repos?**

- **Data-driven** — every insight comes from analyzing real job descriptions and interview data, not guesswork
- **Bilingual** — full English + Chinese coverage ([中文版](zh/README.md))
- **AI-native** — built around LLM, RAG, agents, and modern AI stacks (not retrofitted ML)
- **Salary data** — real compensation benchmarks by company, level, and role
- **Company guides** — Anthropic, OpenAI, Google DeepMind, Meta FAIR, NVIDIA, Databricks, Amazon AGI, and 44 more
- **Real debriefs** — anonymized first-person interview experiences
- **Difficulty-rated** — every question tagged Easy/Medium/Hard with time estimates
- **Study plans** — structured 30/60/90-day plans for different backgrounds
- **Learning paths** — transition guides from DE, DS, MLE, backend, frontend, and PM roles
- **Books by the author** — 30+ role-specific interview playbooks ([full list](BOOKS.md))

---

## Contents

- [The AI Engineer Role](#the-ai-engineer-role)
- [Interview Preparation](#interview-preparation)
- [Learning Paths](#learning-paths)
- [Portfolio](#portfolio)
- [Job Market Data](#job-market-data)
- [Study Plans](#study-plans)
- [Salary & Compensation](#salary--compensation)
- [Company-Specific Guides](#company-specific-guides)
- [Real Interview Debriefs](#real-interview-debriefs)
- [LLM Fundamentals & GenAI](#llm-fundamentals--genai)
- [ML System Design](#ml-system-design)
- [Classical ML & Statistics](#classical-ml--statistics)
- [Coding for ML/AI Roles](#coding-for-mlai-roles)
- [Behavioral Questions for AI Roles](#behavioral-questions-for-ai-roles)
- [LLM Evaluation & Testing](#llm-evaluation--testing)
- [AI Safety & Ethics](#ai-safety--ethics)
- [Tools & Frameworks](#tools--frameworks)
- [Books & Courses](#books--courses)
- [Awesome Resources](#awesome-resources)
- [Communities & Forums](#communities--forums)
- [Complete Interview Prep Library](#complete-interview-prep-library)
- [Contributing](#contributing)

---

## The AI Engineer Role

Understanding what the role actually is — based on analysis of 2,445 real job descriptions.

- [My vision of the role](role/01-my-vision.md) — how AI engineering compares with DS/ML/DE roles, CRISP-DM for AI
- [Skills analysis](role/02-skills.md) — top skills, job types, cloud platforms, frameworks extracted from job postings
- [Responsibilities](role/03-responsibilities.md) — patterns extracted from 5,694+ job responsibilities
- [Use cases](role/04-use-cases.md) — 4,525 real use cases showing what companies build with AI
- [Reality vs. job postings](role/05-reality-vs-postings.md) — what candidates experience vs. what's advertised

---

## Interview Preparation

Everything you need to prepare, from process overview to company-specific data.

- [Interview process](interview/01-interview-process.md) — common patterns, step counts, time estimates, AI use in hiring, key takeaways
- [Interview questions](interview/02-questions.md) — consolidated from 100+ sources
  - [Theory](interview/questions/theory.md) — LLMs, RAG, agents, ML fundamentals, company-specific questions
  - [AI system design](interview/questions/04-ai-system-design.md) — system design for AI applications
  - [Behavioral](interview/questions/05-behavioral.md) — values, leadership, problem-solving
- [Skills that get you hired](interview/03-get-hired.md) — baseline expectations, differentiators, and portfolio strategy
- [After the interview](interview/04-after-the-interview.md) — handling offers, rejections, and salary negotiation
- [Interview trends](interview/05-trends.md) — realistic assessments, AI cheating, AI-proctored rounds
- [Company-by-company data](interview/data/) — individual interview process descriptions for 51 companies, linked to source job postings

---

## Learning Paths

What to learn and in what order, based on where you're coming from.

- [General learning path](learning-paths/) — core skills and recommended order
- [From Data Engineer](learning-paths/from-data-engineer.md) — smoothest transition, 3-4 months
- [From Data Scientist](learning-paths/from-data-scientist.md) — evaluation is your superpower, add engineering
- [From ML Engineer](learning-paths/from-ml-engineer.md) — easiest transition, replace model call with API call
- [From Backend Engineer](learning-paths/from-backend-engineer.md) — 2-3 months, add AI on top of engineering
- [From Frontend Engineer](learning-paths/from-frontend-engineer.md) — backend first, then AI, unique full-stack advantage
- [From Product Manager](learning-paths/from-pm.md) — leverage product sense, add technical depth

---

## Portfolio

- [Project ideas](portfolio/) — real project examples that demonstrate AI engineering skills, mapped to frequently-requested patterns from job descriptions

---

## Job Market Data

2,445 job descriptions scraped from builtin.com covering LA, NY, London, Amsterdam, Berlin, and India.

- [Structured job descriptions](job-market/data_structured/) — YAML files grouped by scrape date
- [Raw extracted postings](job-market/data_raw/) — original extracted data grouped by scrape date

---

## Study Plans

### 30-Day Intensive (Active Job Seekers)

| Week | Focus | Daily Time | Key Activities |
|------|-------|-----------|----------------|
| 1 | Foundations | 3-4 hrs | ML fundamentals review, LLM architecture deep-dive, 2 LeetCode/day |
| 2 | System Design | 3-4 hrs | 1 ML system design case/day, RAG/agent architecture patterns |
| 3 | Behavioral + Company | 2-3 hrs | STAR stories for AI context, target company research, mock interviews |
| 4 | Mock + Polish | 2-3 hrs | 2 mock interviews/day, weak area review, offer negotiation prep |

### 60-Day Balanced (Working Professionals)

| Phase | Weeks | Focus | Daily Time |
|-------|-------|-------|-----------|
| Build | 1-3 | ML/DL fundamentals, LLM internals, coding patterns | 1.5-2 hrs |
| Apply | 4-6 | System design cases, behavioral prep, resume optimization | 1.5-2 hrs |
| Sharpen | 7-8 | Mock interviews, company-specific prep, negotiation practice | 2 hrs |

### 90-Day Career Switcher

**From Backend Engineering:** Focus weeks 1-4 on ML fundamentals and math (linear algebra, probability, optimization). Weeks 5-8 on ML system design — your distributed systems knowledge is directly transferable. Weeks 9-12 on GenAI-specific topics (transformers, RLHF, evaluation).

**From Data Science:** Skip classical ML review. Focus weeks 1-3 on engineering practices (MLOps, CI/CD for models, production serving). Weeks 4-8 on LLM-specific system design. Weeks 9-12 on coding (LeetCode ML patterns) and behavioral.

**From Academia:** Focus weeks 1-4 on industry framing (business impact, production constraints, cost modeling). Weeks 5-8 on system design (scale, latency, reliability — not just accuracy). Weeks 9-12 on behavioral (translate research into STAR stories) and salary negotiation.

---

## Salary & Compensation

### AI/ML Engineer Compensation (2025-2026 US Market)

| Company | Level | Role | Base | Stock (annual) | Bonus | Total TC |
|---------|-------|------|------|---------------|-------|----------|
| Google | L4 (mid) | MLE | $160-185K | $80-120K | 15% | $280-380K |
| Google | L5 (senior) | MLE | $195-230K | $150-250K | 15% | $400-550K |
| Google | L6 (staff) | MLE | $240-280K | $250-450K | 15% | $570-830K |
| Meta | E4 (mid) | MLE | $165-190K | $80-130K | 10% | $280-390K |
| Meta | E5 (senior) | MLE | $200-240K | $150-300K | 15% | $410-620K |
| Meta | E6 (staff) | MLE | $250-300K | $300-500K | 20% | $630-900K |
| Amazon | L5 (mid) | Applied Scientist | $150-175K | $60-100K | sign-on | $240-330K |
| Amazon | L6 (senior) | Applied Scientist | $175-210K | $120-200K | sign-on | $340-480K |
| OpenAI | L3 (mid) | Research Engineer | $200-250K | PPUs | — | $350-600K+ |
| OpenAI | L4 (senior) | Research Engineer | $275-350K | PPUs | — | $500K-1M+ |
| Anthropic | Mid | Research Engineer | $200-260K | equity | — | $350-550K |
| Anthropic | Senior | Research Engineer | $275-350K | equity | — | $500-800K+ |
| NVIDIA | Mid | ML Engineer | $160-200K | $80-140K | 10% | $280-400K |
| NVIDIA | Senior | ML Engineer | $200-250K | $150-300K | 15% | $400-640K |
| Databricks | Mid | ML Engineer | $170-200K | $100-160K | — | $300-400K |
| Databricks | Senior | ML Engineer | $210-260K | $180-350K | — | $430-680K |

*Data sourced from [levels.fyi](https://levels.fyi), Blind, and public H1B records. Ranges represent 25th-75th percentile. Stock values fluctuate.*

### Role Differentiation

| Role | Core Interview Focus | Typical Companies |
|------|---------------------|-------------------|
| **ML Engineer (MLE)** | ML system design, production ML, MLOps, coding | All Big Tech, startups |
| **Applied Scientist** | Research depth, paper implementation, novel methods | Amazon, Microsoft, Meta |
| **AI Engineer** | LLM integration, RAG, agents, prompt engineering, evaluation | OpenAI, Anthropic, startups |
| **Research Scientist** | Novel research, paper publication, experimental design | DeepMind, FAIR, Anthropic |
| **MLOps Engineer** | Infrastructure, pipelines, monitoring, serving systems | All companies with ML at scale |

### Negotiation Resources

- [Ten Rules for Negotiating a Job Offer](https://haseebq.com/my-ten-rules-for-negotiating-a-job-offer/) - Haseeb Qureshi's viral negotiation guide.
- [Levels.fyi Negotiation Guide](https://www.levels.fyi/blog/how-to-negotiate-salary.html) - Data-backed negotiation strategies.
- [Rora Negotiation](https://www.teamrora.com/) - Free negotiation coaching for Big Tech offers.
- [Candor Salary Negotiation](https://candor.co/guides/salary-negotiation) - Step-by-step negotiation framework.

---

## Company-Specific Guides

### Anthropic

**Interview Process:** Recruiter screen -> Technical phone screen (coding + ML) -> Onsite (4-5 rounds: coding, ML depth, system design, research discussion, values/behavioral).

**What They Look For:** Deep understanding of AI safety, alignment research, and responsible AI development. Strong coding + ML fundamentals. Passion for building safe, beneficial AI systems.

**Key Topics:** Constitutional AI, RLHF/DPO, red-teaming, interpretability, scaling laws, evaluation methodology. Be prepared to discuss alignment research papers.

**Resources:** [Anthropic Research](https://www.anthropic.com/research), [Claude Documentation](https://docs.anthropic.com/), [Core Views on AI Safety](https://www.anthropic.com/news/core-views-on-ai-safety)

### OpenAI

**Interview Process:** Recruiter screen -> Technical screen (coding) -> Onsite (4-6 rounds: coding, ML/AI depth, system design, past project deep-dive, behavioral).

**What They Look For:** Strong engineering fundamentals combined with deep AI/ML knowledge. Ability to work on novel problems with ambiguity. Track record of shipping AI products or publishing research.

**Key Topics:** Transformer architectures, scaling laws, RLHF, multi-modal models, inference optimization, evaluation design. Expect questions about GPT architecture and training methodology.

**Resources:** [OpenAI Research](https://openai.com/research/), [OpenAI Cookbook](https://cookbook.openai.com/), [API Documentation](https://platform.openai.com/docs)

### Google DeepMind

**Interview Process:** Recruiter screen -> Phone screens (2: coding + ML) -> Onsite (5 rounds: 2 coding, ML breadth, ML depth/system design, Googleyness/leadership).

**What They Look For:** Strong algorithmic fundamentals (L5+ needs system design). Research depth in at least one area (NLP, CV, RL, optimization). Publication track record valued but not required for engineering roles.

**Key Topics:** Transformer variants, reinforcement learning, optimization theory, distributed training, Gemini/PaLM architecture, TPU programming.

**Resources:** [DeepMind Publications](https://deepmind.google/research/publications/), [Google AI Blog](https://blog.research.google/)

### Meta FAIR / GenAI

**Interview Process:** Recruiter screen -> Phone screen (coding) -> Onsite (4-5 rounds: 2 coding, ML system design, ML depth, behavioral).

**What They Look For:** Strong coding (data structures + algorithms at medium-hard LeetCode level). ML system design at scale (billions of users). Experience with large-scale distributed training.

**Key Topics:** Recommendation systems, ranking models, Llama model family, PyTorch ecosystem, multi-modal AI, content understanding at scale.

**Resources:** [Meta AI Research](https://ai.meta.com/research/), [PyTorch Documentation](https://pytorch.org/docs/), [Llama Models](https://ai.meta.com/llama/)

### NVIDIA

**Interview Process:** Recruiter screen -> Technical phone screen -> Onsite (4-5 rounds: coding, ML/DL depth, system design, team fit).

**What They Look For:** Deep understanding of GPU architecture, CUDA programming, model optimization. Experience with inference optimization (TensorRT, Triton). Hardware-software co-design thinking.

**Key Topics:** GPU memory hierarchy, CUDA kernels, mixed-precision training, model parallelism (tensor/pipeline/data), TensorRT optimization, Triton Inference Server.

**Resources:** [NVIDIA Developer Blog](https://developer.nvidia.com/blog), [CUDA Programming Guide](https://docs.nvidia.com/cuda/)

### Databricks

**Interview Process:** Recruiter screen -> Technical screen -> Onsite (4 rounds: coding, ML, system design, behavioral).

**What They Look For:** Data engineering + ML intersection. Experience with large-scale data processing. Understanding of lakehouse architecture, Spark, and MLflow.

**Key Topics:** Spark optimization, Delta Lake, MLflow lifecycle, feature stores, model serving, Unity Catalog, Mosaic ML training infrastructure.

**Resources:** [Databricks Engineering Blog](https://www.databricks.com/blog/category/engineering), [MLflow Documentation](https://mlflow.org/docs/latest/)

### Amazon AGI / AWS AI

**Interview Process:** Recruiter screen -> Phone screen -> Onsite (5 rounds: 2 coding, ML system design, behavioral/LP, hiring manager).

**What They Look For:** Customer obsession applied to AI. LP-driven behavioral answers. Ability to deliver ML solutions at Amazon scale. Bias for action over perfection.

**Key Topics:** 16 Leadership Principles (know them cold), Alexa/Bedrock/SageMaker architecture, recommendation systems, NLP at scale, frugality in model serving.

**Resources:** [Amazon Science](https://www.amazon.science/), [AWS AI/ML Blog](https://aws.amazon.com/blogs/machine-learning/)

> **See also:** [Company-by-company interview data](interview/data/) for detailed process descriptions from 51 companies.

---

## Real Interview Debriefs

> **Note:** These are anonymized first-person accounts. Details have been modified to protect privacy while preserving the learning value. [Submit your own debrief](CONTRIBUTING.md#interview-debriefs)

### Debrief #1: Senior MLE at a Large AI Lab (Offer Received)

**Timeline:** Applied -> Recruiter screen (1 week) -> Phone screen (2 weeks) -> Onsite (3 weeks) -> Offer (1 week). Total: ~7 weeks.

**Rounds:**
1. **Coding (45 min):** Medium LeetCode — graph traversal + optimization. Finished with 10 min to spare. Interviewer tested edge cases.
2. **ML Depth (45 min):** Deep dive on transformer architecture. Asked to explain KV cache, rotary positional embeddings, and flash attention. Follow-up: "How would you modify the attention mechanism for very long contexts?"
3. **System Design (60 min):** "Design a real-time toxicity detection system for a chat platform." Covered data pipeline, model selection, serving architecture, human-in-the-loop feedback, and cost analysis.
4. **Research Discussion (45 min):** Discussed my past project on fine-tuning LLMs for domain-specific tasks. Deep questions on evaluation methodology and failure modes.
5. **Behavioral (45 min):** Standard STAR questions but all AI-contextualized: "Tell me about a time your model caused an unexpected negative impact."

**What Worked:** Quantified everything with numbers. For system design, included a cost model ($/query) which the interviewer specifically called out as strong. Prepared 8 STAR stories specifically about ML projects.

**What I'd Change:** Should have asked more clarifying questions in the system design round — I jumped to architecture too quickly.

### Debrief #2: AI Engineer at a Mid-Stage Startup (Offer Received)

**Timeline:** Referral -> Phone screen (3 days) -> Take-home (1 week deadline) -> Onsite (1 week) -> Offer (2 days). Total: ~3 weeks.

**Rounds:**
1. **Phone Screen (30 min):** Conversational. "What's your experience with RAG?" "Walk me through a production AI system you built." No coding.
2. **Take-Home (4 hours):** Build a RAG pipeline over a provided dataset. Evaluate with precision@5 and answer quality. Submit code + 1-page writeup.
3. **Onsite — Technical Review (60 min):** Walk through take-home code. Deep questions on chunking strategy, embedding choice, and why I used hybrid retrieval.
4. **Onsite — System Design (45 min):** "Design our AI-powered search from scratch." Focused on practical constraints: budget, team size, time to ship.
5. **Onsite — Founder Chat (30 min):** Culture fit, motivation, career goals. "Why a startup over Big Tech?"

**What Worked:** The take-home was my best performing round. I over-invested in evaluation (built a mini eval harness) which impressed them.

**What I'd Change:** Should have researched the company's product more deeply before the founder chat.

---

## LLM Fundamentals & GenAI

### Transformer Architecture & Training

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - The foundational transformer paper. Every AI engineer should understand multi-head attention, positional encoding, and encoder-decoder architecture.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) - Jay Alammar's visual walkthrough — the most accessible explanation of transformer internals.
- [nanoGPT](https://github.com/karpathy/nanoGPT) - Andrej Karpathy's minimal GPT implementation. Build a transformer from scratch to understand it deeply.
- [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course) - Free course covering tokenizers, transformers, fine-tuning, and the Hugging Face ecosystem.
- [Stanford CS324: Large Language Models](https://stanford-cs324.github.io/winter2022/) - Stanford's graduate course on LLM foundations, capabilities, and limitations.

### Retrieval-Augmented Generation (RAG)

- [RAG Paper (Lewis et al.)](https://arxiv.org/abs/2005.11401) - Original RAG paper combining retrieval and generation for knowledge-intensive tasks.
- [LlamaIndex Documentation](https://docs.llamaindex.ai/) - Production RAG framework with indexing, retrieval, and query engine patterns.
- [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/) - End-to-end RAG pipeline with document loaders, embeddings, vector stores, and chains.
- [Pinecone Learning Center](https://www.pinecone.io/learn/) - Vector database fundamentals, embedding models, and retrieval optimization.
- [Advanced RAG Techniques](https://github.com/NirDiamant/RAG_Techniques) - Comprehensive collection of RAG strategies: hybrid search, reranking, query decomposition, and self-RAG.

### AI Agents & Agentic Systems

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/) - Framework for building stateful, multi-actor AI agent applications with cycles and controllability.
- [AutoGen](https://github.com/microsoft/autogen) - Microsoft's framework for multi-agent conversations and task decomposition.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Role-based multi-agent orchestration with task delegation patterns.
- [Building Effective Agents (Anthropic)](https://docs.anthropic.com/en/docs/build-with-claude/agent) - Anthropic's guide to building reliable AI agents with tool use and planning.
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - OpenAI's production framework for building agentic workflows.

### Fine-Tuning & Alignment

- [RLHF Paper (Ouyang et al.)](https://arxiv.org/abs/2203.02155) - InstructGPT paper establishing RLHF as the standard alignment technique.
- [DPO Paper (Rafailov et al.)](https://arxiv.org/abs/2305.18290) - Direct Preference Optimization — simpler alternative to RLHF without a reward model.
- [Hugging Face PEFT](https://huggingface.co/docs/peft) - Parameter-efficient fine-tuning: LoRA, QLoRA, prefix tuning, and adapters.
- [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) - Streamlined fine-tuning for various architectures with support for multi-GPU and cloud training.
- [Constitutional AI (Anthropic)](https://arxiv.org/abs/2212.08073) - Self-supervision approach to AI alignment using principles instead of human feedback.

### Prompt Engineering

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) - Official guide covering chain-of-thought, few-shot, and structured output patterns.
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) - Best practices for getting reliable results from GPT models.
- [Prompt Engineering Guide](https://www.promptingguide.ai/) - Community-maintained comprehensive guide covering techniques, applications, and research.

### Interview Questions — LLM Fundamentals

| # | Question | Difficulty | Time |
|---|----------|-----------|------|
| 1 | Explain the self-attention mechanism. What is the computational complexity and how do techniques like Flash Attention optimize it? | Medium | 15 min |
| 2 | Compare RLHF, DPO, and GRPO for LLM alignment. When would you choose each? | Hard | 20 min |
| 3 | You need to serve a 70B parameter model with <200ms P95 latency. Walk through your optimization strategy (quantization, batching, KV cache, speculative decoding). | Hard | 30 min |
| 4 | Design a RAG pipeline for a legal document search system. How do you handle chunking, embedding model selection, and hybrid retrieval? | Hard | 30 min |
| 5 | What are the tradeoffs between fine-tuning and in-context learning? Give a scenario where each is the right choice. | Medium | 15 min |
| 6 | Explain how LoRA works. Why does it reduce memory requirements? What are its limitations compared to full fine-tuning? | Medium | 15 min |
| 7 | How would you detect and mitigate hallucinations in a production LLM application? | Medium | 20 min |
| 8 | Compare embedding models (OpenAI ada-002, Cohere embed-v3, BGE, E5). How do you evaluate which one is right for your use case? | Medium | 15 min |
| 9 | Explain the difference between AI agents and AI pipelines. When would you use a deterministic workflow vs an agentic loop? | Medium | 15 min |
| 10 | You're building a customer support chatbot. The LLM sometimes reveals internal pricing or policy details it shouldn't. How do you implement guardrails? | Hard | 25 min |

---

## ML System Design

### Framework

Every ML system design answer should cover these 5 areas:

1. **Problem Framing** — What are we optimizing for? What are the business constraints?
2. **Data Pipeline** — How do we collect, clean, label, and store training data at scale?
3. **Model Architecture** — Which model family? Training strategy? Offline vs online learning?
4. **Serving & Inference** — Latency requirements? Batch vs real-time? Caching strategy?
5. **Evaluation & Monitoring** — Offline metrics, online A/B testing, drift detection, alerting.

### Resources

- [Machine Learning Systems Design (Chip Huyen)](https://github.com/chiphuyen/machine-learning-systems-design) - 27 open-ended ML system design questions with a 4-step framework.
- [ML System Design Interview Guide](https://github.com/alirezadir/Machine-Learning-Interviews) - Comprehensive coverage including GenAI and agentic system design (updated 2025).
- [Designing Machine Learning Systems (O'Reilly)](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) by Chip Huyen - The definitive book on production ML systems.
- [System Design for ML Interviews](https://www.educative.io/courses/machine-learning-system-design) - Interactive course with worked examples.
- [ML Design Patterns (Google)](https://github.com/GoogleCloudPlatform/ml-design-patterns) - 30 design patterns for data preparation, model building, and MLOps.

### Worked Example: Design a RAG Pipeline for Legal Document Search

**Problem:** A law firm wants to search 10M legal documents using natural language queries with cited sources.

**Architecture:**
```
Documents -> Chunker (recursive, 512 tokens) -> Embeddings (BGE-large)
                                                      |
User Query -> Query Rewriter -> Hybrid Retrieval (dense + BM25) -> Reranker (cross-encoder)
                                                                          |
                                                              LLM (Claude/GPT-4) + Citations -> Response
```

**Key decisions:**
- **Chunking:** Recursive with 512-token windows, 50-token overlap. Legal docs need section-aware splitting (by clause/paragraph, not arbitrary).
- **Retrieval:** Hybrid (dense embeddings + BM25) outperforms dense-only by 15-20% on legal text. Use Reciprocal Rank Fusion to merge results.
- **Reranking:** Cross-encoder reranker on top-50 retrieved chunks reduces noise before LLM context window.
- **Cost:** At 10M docs x 5 chunks/doc x $0.0001/embedding = $5K one-time. Serving: ~$0.05/query with caching.
- **Evaluation:** Precision@K on golden test set, human eval on citation accuracy, latency P95 < 3s.

### Worked Example: Design an AI Customer Support Agent

**Problem:** E-commerce company wants an AI agent that handles 80% of support tickets autonomously.

**Architecture:**
```
Ticket -> Intent Classifier -> Router
                               |-- FAQ (retrieval from KB) -> Response
                               |-- Order Status (tool call: order API) -> Response
                               |-- Refund (tool call: payment API + approval logic) -> Response
                               +-- Escalation (confidence < 0.85) -> Human Agent
```

**Key decisions:**
- **Tool use:** Agent needs access to order management, payment, and CRM APIs. Each tool has strict input validation and rate limiting.
- **Guardrails:** Never reveal internal pricing logic. Never process refunds > $500 without human approval. PII masking on all logs.
- **Evaluation:** Resolution rate, customer satisfaction score, escalation rate, time-to-resolution. A/B test against human-only baseline.
- **Cost modeling:** GPT-4o at ~$0.03/ticket vs human agent at ~$5/ticket. Break-even at 167 tickets/day.

### Interview Questions — System Design

| # | Question | Difficulty | Time |
|---|----------|-----------|------|
| 1 | Design a real-time content moderation system for a social platform processing 10K posts/minute. | Hard | 45 min |
| 2 | Design a recommendation system that uses LLM reranking on top of traditional collaborative filtering. | Hard | 45 min |
| 3 | Design a multi-modal search engine that handles text, images, and video. | Hard | 45 min |
| 4 | Design a fraud detection system that adapts to new fraud patterns within hours, not weeks. | Hard | 45 min |
| 5 | Design an LLM-powered code review tool for a team of 500 engineers. | Medium | 30 min |

---

## Classical ML & Statistics

### Resources

- [Machine Learning Interview (khangich)](https://github.com/khangich/machine-learning-interview) - 12.6K stars. Covers ML fundamentals, LeetCode for ML, A/B testing, and ML system design with real FAANG offer stories.
- [ML-NLP (NLP-LOVE)](https://github.com/NLP-LOVE/ML-NLP) - Knowledge points + runnable code implementations. Covers classical ML through deep NLP.
- [StatQuest with Josh Starmer](https://www.youtube.com/c/joshstarmer) - The best visual explanations of statistical concepts and ML algorithms on YouTube.
- [An Introduction to Statistical Learning (ISLR)](https://www.statlearning.com/) - Free textbook covering regression, classification, resampling, and unsupervised learning.
- [Mathematics for Machine Learning](https://mml-book.github.io/) - Free textbook covering linear algebra, analytic geometry, probability, and optimization.
- [Data Science Interview Resources](https://github.com/rbhatia46/Data-Science-Interview-Resources) - Broad algorithm coverage from logistic regression through deep learning, with Kaggle practice links.

### High-Frequency Questions

| # | Question | Difficulty | Time |
|---|----------|-----------|------|
| 1 | Explain bias-variance tradeoff. How does it relate to model complexity and regularization? | Easy | 10 min |
| 2 | When would you use L1 vs L2 regularization? What does each do geometrically? | Easy | 10 min |
| 3 | Explain gradient boosting. How does XGBoost differ from random forests? | Medium | 15 min |
| 4 | What is the curse of dimensionality? How do PCA and t-SNE address it differently? | Medium | 15 min |
| 5 | Design an A/B test for a new ML-powered feature. How do you handle multiple comparisons and determine sample size? | Hard | 20 min |

---

## Coding for ML/AI Roles

- [LeetCode](https://leetcode.com) - 3000+ problems with company tags. Focus on medium-difficulty problems tagged by target company.
- [NeetCode](https://neetcode.io) - Curated roadmap of 150 problems organized by pattern. Best video explanations in the space.
- [Grind 75](https://www.techinterviewhandbook.org/grind75) - Updated Blind 75. Customize by available time (1 week to 3 months).
- [LeetCode Patterns](https://github.com/seanprashad/leetcode-patterns) - Problems categorized by pattern: sliding window, two pointer, BFS/DFS, dynamic programming.
- [ML Coding Challenges](https://github.com/alirezadir/Machine-Learning-Interviews#2-ml-coding) - Implement backprop, k-means, attention, gradient descent, decision tree from scratch.

### ML-Specific Coding

| # | Task | Difficulty | What It Tests |
|---|------|-----------|--------------|
| 1 | Implement multi-head attention from scratch in NumPy | Hard | Transformer internals |
| 2 | Write a basic tokenizer (BPE) | Medium | NLP fundamentals |
| 3 | Implement K-means clustering with NumPy | Easy | Unsupervised learning basics |
| 4 | Build a simple neural network with only NumPy (forward + backward pass) | Medium | Backpropagation understanding |
| 5 | Implement beam search for text generation | Medium | Decoding strategies |

---

## Behavioral Questions for AI Roles

Most repos treat behavioral as an afterthought. In reality, behavioral rounds are **elimination rounds** — technical skills get you to the final round, but behavioral determines the offer.

### AI-Context Behavioral Questions

| # | Question | Framework | Difficulty |
|---|----------|----------|-----------|
| 1 | Tell me about a time your model failed in production. What happened, and what did you change? | STAR + Root Cause | Medium |
| 2 | Describe a situation where you disagreed with a researcher about model architecture. How did you resolve it? | STAR + Conflict Resolution | Medium |
| 3 | You shipped a feature powered by an LLM, but users complained about hallucinations. Walk me through your response. | STAR + Incident Response | Hard |
| 4 | Tell me about a time you had to explain a complex ML concept to a non-technical stakeholder. | STAR + Communication | Easy |
| 5 | Describe a project where you had to balance model accuracy against serving cost or latency. | STAR + Tradeoffs | Medium |
| 6 | You're leading an ML project and realize midway that the approach won't work. What do you do? | STAR + Decision Making | Hard |
| 7 | Tell me about a time you had to work with messy, incomplete, or biased data. How did you handle it? | STAR + Data Quality | Medium |
| 8 | Describe a situation where you had to choose between building a custom model vs using an off-the-shelf API. | STAR + Build vs Buy | Medium |
| 9 | You joined a new team and found their ML pipeline had significant technical debt. How did you approach improving it? | STAR + Influence Without Authority | Hard |
| 10 | Tell me about a time you mentored a junior engineer on an ML project. What was the outcome? | STAR + Leadership | Medium |
| 11 | Describe a project where you had to make a decision with incomplete information. How did you reduce uncertainty? | STAR + Ambiguity | Hard |
| 12 | You're responsible for an AI feature that a customer found biased. How did you investigate and address it? | STAR + Ethics | Hard |
| 13 | Tell me about a time you proactively identified a risk in an ML system before it caused issues. | STAR + Ownership | Medium |
| 14 | Describe how you handled a situation where training data was unexpectedly leaked or compromised. | STAR + Security | Hard |
| 15 | You proposed a novel approach that your team was skeptical about. How did you convince them? | STAR + Persuasion | Medium |

### STAR Framework for AI Roles

**Situation:** Set the scene in 2-3 sentences. Include the AI/ML context (model type, data scale, business impact).

**Task:** What was your specific responsibility? Quantify the goal (improve latency by 50%, reduce false positives by 30%).

**Action:** What did YOU do? Use "I" not "we." Be specific about technical decisions (chose LoRA over full fine-tuning because...).

**Result:** Quantify the outcome. Business metrics > model metrics. "Reduced customer churn by 12%" beats "improved F1 by 0.03."

---

## LLM Evaluation & Testing

### Resources

- [HELM (Stanford)](https://crfm.stanford.edu/helm/) - Holistic evaluation of language models across 42 scenarios.
- [LMSys Chatbot Arena](https://chat.lmsys.org/) - Crowdsourced LLM leaderboard via blind pairwise comparison.
- [Inspect AI (UK AISI)](https://inspect.ai-safety-institute.org.uk/) - Open-source framework for LLM evaluation with built-in benchmarks.
- [DeepEval](https://github.com/confident-ai/deepeval) - Unit testing framework for LLM applications — test hallucination, relevance, toxicity.
- [Ragas](https://docs.ragas.io/) - Evaluation framework specifically for RAG pipelines.

### Interview Questions — Evaluation

| # | Question | Difficulty | Time |
|---|----------|-----------|------|
| 1 | How would you evaluate a customer-facing LLM chatbot? What metrics would you track offline vs online? | Medium | 20 min |
| 2 | Design a red-teaming strategy for a new LLM product launch. | Hard | 25 min |
| 3 | You've fine-tuned a model and it scores better on benchmarks but users report worse quality. What's happening? | Hard | 20 min |
| 4 | Compare BLEU, ROUGE, BERTScore, and LLM-as-judge. When is each appropriate? | Medium | 15 min |
| 5 | How would you design an A/B test for an LLM feature when responses are non-deterministic? | Hard | 20 min |

---

## AI Safety & Ethics

- [Anthropic Core Views on AI Safety](https://www.anthropic.com/news/core-views-on-ai-safety) - Anthropic's framework for thinking about AI safety risks.
- [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence) - US government framework for AI risk management.
- [EU AI Act Summary](https://artificialintelligenceact.eu/) - Overview of the EU's risk-based AI regulation framework.
- [Responsible AI Practices (Google)](https://ai.google/responsibility/responsible-ai-practices/) - Practical guidelines for building fair, interpretable, and safe AI.
- [AI Safety Fundamentals (BlueDot Impact)](https://aisafetyfundamentals.com/) - Free course covering alignment, interpretability, and governance.

---

## Tools & Frameworks

### Training & Fine-Tuning
- [PyTorch](https://pytorch.org/) - De facto standard for ML research and production.
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/) - Pre-trained models and fine-tuning utilities.
- [DeepSpeed](https://github.com/microsoft/DeepSpeed) - Microsoft's distributed training library for efficiency at scale.
- [Ray Train](https://docs.ray.io/en/latest/train/train.html) - Distributed ML training framework.

### Serving & Inference
- [vLLM](https://github.com/vllm-project/vllm) - High-throughput LLM serving with PagedAttention.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) - NVIDIA's optimized LLM inference library.
- [Triton Inference Server](https://github.com/triton-inference-server/server) - Production model serving with multi-framework support.
- [Ollama](https://ollama.ai/) - Run LLMs locally with one command.

### Orchestration & Agents
- [LangChain](https://www.langchain.com/) - Framework for building LLM-powered applications.
- [LlamaIndex](https://www.llamaindex.ai/) - Data framework for LLM applications (RAG, agents, queries).
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Microsoft's SDK for integrating AI into applications.

### Monitoring & Evaluation
- [Weights & Biases](https://wandb.ai/) - Experiment tracking, model registry, and production monitoring.
- [MLflow](https://mlflow.org/) - Open-source ML lifecycle management.
- [Langfuse](https://langfuse.com/) - Open-source LLM observability and evaluation.
- [Arize AI](https://arize.com/) - ML observability with drift detection and explainability.

### Vector Databases
- [Pinecone](https://www.pinecone.io/) - Managed vector database for similarity search.
- [Weaviate](https://weaviate.io/) - Open-source vector database with hybrid search.
- [Milvus](https://milvus.io/) - Open-source vector database for scalable similarity search.
- [Chroma](https://www.trychroma.com/) - Lightweight embedding database for AI applications.

---

## Books & Courses

### Community Picks

**Books**
- [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) by Chip Huyen - The best book on production ML systems.
- [Deep Learning](https://www.deeplearningbook.org/) by Goodfellow, Bengio, Courville - The comprehensive reference for DL theory.
- [Hands-On Machine Learning](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/) by Aurelien Geron - Practical ML with Scikit-Learn, Keras, and TensorFlow.
- [Build a Large Language Model (From Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch) by Sebastian Raschka - Build GPT from the ground up.

**Courses**
- [Stanford CS229: Machine Learning](https://cs229.stanford.edu/) - Andrew Ng's foundational ML course. Free lecture videos.
- [Stanford CS324: Large Language Models](https://stanford-cs324.github.io/winter2022/) - Graduate course on LLM foundations.
- [Fast.ai Practical Deep Learning](https://course.fast.ai/) - Top-down, practical approach to deep learning. Free.
- [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/) - Production LLM engineering from UC Berkeley.
- [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/) - Free short courses on RAG, fine-tuning, agents, and evaluation.

### Books by the Author

> *Disclosure: The following are written by the maintainer of this repo. They are listed separately from community picks for transparency.*

**AI & ML Roles**
- [The 0-to-1 AI Engineer Interview Playbook](https://www.amazon.com/dp/B0H2CML9XD) - GenAI interview prep: LLM system design, RAG, agents, evaluation, behavioral for AI roles.
- [The 0-to-1 ML Engineer Interview Playbook](https://www.amazon.com/dp/B0H256Z1MF) - Production ML systems, model training, and MLE-specific system design.
- [The 0-to-1 Data Scientist Interview Playbook](https://www.amazon.com/dp/B0H1NWZB2R) - Statistics, ML fundamentals, case studies, and A/B testing for DS roles.
- [The 0-to-1 Data Engineer Interview Playbook](https://www.amazon.com/dp/B0H249WDPZ) - SQL, data pipelines, data modeling, and cloud infrastructure.

**Engineering & Leadership**
- [The 0-to-1 SWE Interview Playbook](https://www.amazon.com/dp/B0H1F83LCM) - Coding interviews, system design, behavioral, and offer negotiation.
- [The 0-to-1 Engineering Manager Interview Playbook](https://www.amazon.com/dp/B0H259JRYG) - EM interviews at Google, Meta, Amazon, Stripe.
- [The 0-to-1 TPM Interview Playbook](https://www.amazon.com/dp/B0H25CR241) - Technical Program Manager interviews at Big Tech.
- [The 0-to-1 SRE/DevOps Interview Playbook](https://www.amazon.com/dp/B0H1C8ZKSN) - Systems thinking, incident response, Kubernetes.
- [The 0-to-1 Solutions Architect Interview Playbook](https://www.amazon.com/dp/B0H295RKHP) - AWS, GCP, Azure system design.
- [The 0-to-1 Security Engineer Interview Playbook](https://www.amazon.com/dp/B0H34M7WXC) - Security engineering interviews.

**Product & Design**
- [The 0-to-1 PM Interview Playbook](https://www.amazon.com/dp/B0GWWJQ2S3) - Product sense, metrics, strategy, behavioral.
- [The 0-to-1 Product Design Interview Playbook](https://www.amazon.com/dp/B0H2FY3BJM) - UX challenges, portfolio reviews, app critiques.
- [The 0-to-1 PMM Interview Playbook](https://www.amazon.com/dp/B0H2CX1BH2) - GTM strategy, positioning, marketing.

---

## Awesome Resources

Curated collection of resources compiled from researching content for this field guide:

- [Practitioner interview stories](awesome.md#ai-interview-experiences) - first-person accounts from candidates and interviewers
- [AI system design guides](awesome.md#architecture-lessons-and-patterns-2025-2026) - production architecture patterns and lessons learned
- [Company engineering blogs](awesome.md) - technical blogs from AI-first companies
- [Books and courses](awesome.md) - additional learning resources
- [Case study collections](awesome.md) - real-world AI deployment case studies

See **[awesome.md](awesome.md)** for the complete list.

---

## Complete Interview Prep Library

> Beyond AI/ML — the full 0-to-1 Playbook series covers 30+ career paths. [See all books](BOOKS.md)

<details>
<summary><strong>Finance & Consulting</strong></summary>

- [The 0-to-1 Quant Interview Playbook](https://www.amazon.com/dp/B0H2CYVXTR) - Quantitative finance interviews: brainteasers, probability, stochastic calculus.
- [The 0-to-1 Hedge Fund Interview Playbook](https://www.amazon.com/dp/B0H2G1W19M) - Hedge fund interviews: investment thesis, stock pitch, portfolio construction.
- [The 0-to-1 Investment Banking Interview Playbook](https://www.amazon.com/dp/B0H2C1MRWS) - IB interviews: technicals, deal analysis, fit questions.
- The 0-to-1 Private Equity Interview Playbook - PE interviews: LBO modeling, case studies, operational improvement. *(Coming Soon)*
- The 0-to-1 Venture Capital Interview Playbook - VC interviews: market sizing, deal sourcing, portfolio strategy. *(Coming Soon)*
- The 0-to-1 Consulting Interview Playbook - Management consulting: case interviews, market sizing, frameworks. *(Coming Soon)*

</details>

<details>
<summary><strong>Academic Admissions</strong></summary>

- [Harvard Admissions Playbook](https://www.amazon.com/dp/) - Harvard undergraduate admissions strategy.
- [MIT Admissions Playbook](https://www.amazon.com/dp/) - MIT undergraduate admissions strategy.
- [Stanford Admissions Playbook](https://www.amazon.com/dp/) - Stanford undergraduate admissions strategy.
- [Yale Admissions Playbook](https://www.amazon.com/dp/) - Yale undergraduate admissions strategy.
- [UC System Admissions Playbook](https://www.amazon.com/dp/) - UC system admissions strategy.

</details>

<details>
<summary><strong>More Tech Roles</strong></summary>

For the complete list of all 30+ interview playbooks across tech, finance, consulting, law, and academic admissions, see [BOOKS.md](BOOKS.md).

</details>

---

## Communities & Forums

- [r/MachineLearning](https://www.reddit.com/r/MachineLearning/) - Reddit's ML research community. Papers, discussions, and career advice.
- [r/cscareerquestions](https://www.reddit.com/r/cscareerquestions/) - Career discussions, interview experiences, and offer negotiations.
- [r/artificial](https://www.reddit.com/r/artificial/) - Broader AI discussions including industry trends and product launches.
- [Blind](https://www.teamblind.com) - Anonymous verified-employee forum for TC, interviews, and career.
- [Hacker News "Who is Hiring?"](https://news.ycombinator.com/) - Monthly job threads with direct hiring manager access.
- [ML Collective Discord](https://mlcollective.org/) - Research community for ML practitioners.
- [Weights & Biases Community](https://wandb.ai/community) - ML practitioner community with events and discussions.
- [Hugging Face Discord](https://huggingface.co/join/discord) - Open-source AI community with model discussions.
- [知乎 ML Topics](https://www.zhihu.com/topic/19559450) - Chinese Q&A platform for ML career and interview discussions.
- [掘金 (Juejin)](https://juejin.cn/) - Chinese developer community with AI/ML content.
- [Datawhale](https://github.com/datawhalechina) - China's largest AI learner community.

---

## Contributing

Contributions welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

### How to Contribute

1. **Add a resource:** Fork this repo, add entry in appropriate section, submit PR
2. **Submit an interview debrief:** Use the [debrief template](CONTRIBUTING.md#interview-debriefs), submit PR
3. **Translate to Chinese:** Help expand the [zh/](zh/) directory
4. **Fix a broken link:** Found a dead link? Open an issue or submit a fix

### Quality Standards

- Resources must be actively maintained (updated within 12 months)
- Free resources are preferred; paid resources clearly marked
- No affiliate or tracking links in community-curated sections
- Interview debriefs must be anonymized (no real names, modified company details)

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This work is licensed under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).
