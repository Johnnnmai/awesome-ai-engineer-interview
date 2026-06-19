# AI Engineering Interview Questions — Theory & Technical

Consolidated from 100+ sources including blog posts, YouTube transcripts, Reddit threads, Medium articles, and interview guides. Every question was extracted from actual interview experiences or preparation materials.

## LLM Fundamentals

- How do LLMs work? `Easy` `15 min` [^proptech-founder-2]
- How do transformers work? `Medium` `25 min` [^proptech-founder-2] [^reddit-genai-consulting] [^reddit-ai-eng-questions]
- What is tokenization and how does it affect LLM performance? `Easy` `15 min` [^fahd-mirza] [^glassdoor-quantiphi] [^glassdoor-asapp]
- What is the difference between pre-training and fine-tuning? `Easy` `15 min` [^fahd-mirza] [^reddit-capital-one] [^glassdoor-cognida]
- Explain context windows and their limitations. `Easy` `15 min` [^fahd-mirza] [^exponent-openai-ml]
- What are scaling laws and why do they matter? `Medium` `20 min` [^fahd-mirza] [^reddit-llm-interview-prep]
- What is temperature and top-p sampling? How do they affect outputs? `Easy` `15 min` [^fahd-mirza] [^reddit-genai-consulting] [^x-aryyann8]
- Explain few-shot learning and chain-of-thought prompting. `Easy` `15 min` [^fahd-mirza] [^reddit-genai-consulting] [^reddit-ai-eng-questions]
- What is KV cache? How does it help in LLM inference? `Medium` `20 min` [^igotanoffer] [^reddit-llm-interview-prep]
- Can you describe the difference between GenAI and traditional programming in the context of solving a real-world problem? `Easy` `15 min` [^proptech-founder-1]
- How do you ensure the outputs from large language models are consistent and accurate, especially when dealing with complex multi-step workflows? `Medium` `20 min` [^proptech-founder-1]
- What's an RAG model? Explain the complete process. `Medium` `25 min` [^khushal-kumar] [^reddit-ai-eng-questions] [^reddit-genai-consulting]
- What are embeddings? `Easy` `15 min` [^khushal-kumar] [^reddit-ai-eng-questions] [^reddit-genai-consulting]
- How does chunking happen? `Easy` `15 min` [^khushal-kumar] [^reddit-ai-eng-questions] [^reddit-genai-consulting]
- What is the difference between discriminative and generative models? `Easy` `15 min` [^reddit-genai-consulting]
- What is graph RAG? How does it differ from standard RAG? `Hard` `30 min` [^reddit-ai-eng-questions]
- What is reflection in the context of LLM agents? `Medium` `20 min` [^reddit-ai-eng-questions]
- Explain KL divergence. `Medium` `20 min` [^reddit-clear-genai]
- What is the difference between symbolic and connectionist AI? `Medium` `20 min` [^reddit-hiring-process]
- Describe the types of text summarization techniques and when you'd use each. `Medium` `20 min` [^reddit-hiring-process]
- How do you do memory management and context management with LLMs? `Medium` `25 min` [^reddit-ai-eng-questions]
- What is the self-attention mechanism? How does it differ from multi-head attention? `Medium` `25 min` [^sundeep-teki]
- What is grouped query attention and how does it differ from standard multi-head attention? `Hard` `30 min` [^mimansa-jaiswal]
- What are the differences between BPE, WordPiece, and character-level tokenization? What are the trade-offs? `Medium` `25 min` [^fahd-mirza]
- Explain the difference between encoder-only, decoder-only, and encoder-decoder Transformer architectures. When would you use each? `Medium` `25 min` [^tidorp] [^hn-46319888] [^reddit-llm-interview-prep]
- Why are decoder-only models dominant even for non-generation tasks? `Medium` `20 min` [^reddit-llm-interview-prep]
- What is positional encoding and why is it needed in Transformers? `Medium` `20 min` [^linkjob-openai]
- What are the key MMLU, BigBench, and HumanEval benchmarks? What does each measure and what are its limitations? `Medium` `20 min` [^fahd-mirza]
- What is the difference between RLHF and DPO? When would you prefer one over the other? `Hard` `35 min` [^mimansa-jaiswal]
- What is Mixture of Experts (MoE)? How does it improve efficiency? `Hard` `30 min` [^mimansa-jaiswal]
- How do LLMs actually generate text? Explain the autoregressive decoding process. `Medium` `20 min` [^hn-46319888] [^llmgenai]
- What are decoding strategies like beam search, top-k, and top-p? When do you use each? `Medium` `25 min` [^mimansa-jaiswal]
- What is FlashAttention and how does it work? `Hard` `30 min` [^reddit-llm-interview-prep]
- Why is LLM inference memory-bounded? `Medium` `20 min` [^reddit-llm-interview-prep]
- How do stop sequences work in LLMs? `Easy` `10 min` [^reddit-llm-interview-prep]
- What is the context window and what happens when you exceed it? How do you handle long documents? `Medium` `20 min` [^hn-46319888] [^llmgenai]
- What risks arise from applying a general-purpose tokenizer to specialized domains like legal or medical text? `Medium` `20 min` [^x-ali-shohadaee]

## RAG Systems

- Design a RAG system for a customer support chatbot. How do you evaluate it? `Hard` `45 min` [^process-analysis] [^reddit-genai-consulting] (reported across multiple companies)
- How would you design an LLM-powered enterprise search system? `Hard` `45 min` [^igotanoffer]
- Design a generative AI document-processing pipeline for unstructured data (emails, PDFs, images) to automate workflows like claims processing. `Hard` `45 min` [^igotanoffer]
- How would you use GPT-4 to generate accurate answers based on proprietary documents? `Medium` `25 min` [^interviewnode]
- Design a generative QA assistant for your company's knowledge base. `Hard` `40 min` [^interviewnode]
- You're making a system that processes huge PDF reports. How would you handle the problem of not keeping an entire report's context when splitting a document for a chatbot? `Medium` `25 min` [^proptech-founder-1]
- How would you efficiently generate and store embeddings for products and queries in a chatbot application? `Medium` `25 min` [^proptech-founder-2]
- How would you handle the problem of a model hallucinating when no information is found in the given context? `Medium` `25 min` [^proptech-founder-2]
- What retrieval-augmented generation (RAG) projects have you worked on? `Easy` `15 min` [^igotanoffer]
- Design a question-answering system over internal documentation. `Hard` `40 min` [^system-design-handbook]
- How do you ensure the quality of data that an LLM interacts with? `Medium` `20 min` [^proptech-founder-2]
- Compare sparse vs. dense retrieval. When would you use each? `Medium` `25 min` [^reddit-clear-genai]
- What are common RAG failure points and how do you debug them? `Medium` `25 min` [^reddit-clear-genai] [^reddit-grilled-rag] [^x-athletickoder-2]
- How do you protect sensitive/confidential data in a RAG pipeline? `Medium` `20 min` [^reddit-grilled-rag]
- What vector databases have you used? Which ones and why? `Easy` `15 min` [^reddit-ai-eng-questions] [^promptlayer] [^llmgenai]
- You have a financial report where page 1 says "all amounts in thousands." How do you handle document-wide context when chunking page by page? `Medium` `25 min` [^proptech-founder-1]
- What is hybrid search? When would you combine vector search with keyword search (BM25)? `Medium` `20 min` [^designgurus-rag]
- What is re-ranking and why is it needed on top of vector retrieval? Explain cross-encoder vs. bi-encoder. `Medium` `25 min` [^designgurus-rag]
- How do you scale a RAG system to 10M+ articles? Discuss sharding, caching, and retrieval optimization. `Hard` `40 min` [^bhavishya-pandit]
- Your RAG system returns relevant documents but users still can't find the answer. How do you transform it from a search engine into an answer engine? `Hard` `35 min` [^hitendra-patel]
- How do you evaluate a RAG pipeline? What metrics would you use? (NDCG, MRR, precision@k, recall) `Hard` `35 min` [^mimansa-jaiswal]
- How do you handle citations and source attribution in a RAG system? `Medium` `20 min` [^proptech-founder-1]
- How does Approximate Nearest Neighbor (ANN) search work? Explain HNSW indexing. `Hard` `30 min` [^designgurus-rag]
- Where do embeddings fail? Discuss negation, temporal reasoning, and precision requirements. `Hard` `30 min` [^techeon]
- What is semantic caching and how can it reduce cost and latency in a RAG system? `Medium` `20 min` [^designgurus-rag] [^hn-44796765]
- Design a RAG system that maintains context across multi-turn conversations. `Hard` `40 min` [^hn-44875256]
- What are the key tradeoffs when designing a RAG system (latency vs accuracy, chunk size vs context, cost vs quality)? `Medium` `25 min` [^reddit-genai-product]
- How do you optimize RAG latency in production? `Medium` `25 min` [^x-aryyann8]

## Agents and Tool Use

- What is an AI agent and what is its role in a broader system? `Easy` `15 min` [^proptech-founder-1]
- What's the difference between an agent and a simple LLM chain? `Medium` `20 min` [^process-analysis] (reported across multiple companies)
- What makes an AI system truly agentic and what does not qualify? `Medium` `20 min` [^techeon] [^reddit-ai-agentic] [^reddit-devsindia-genai] [^hn-43884713] [^hn-42431361] [^x-aryyann8]
- When is an agentic architecture the wrong solution? `Medium` `20 min` [^techeon] [^reddit-csuk-agents]
- How do you define and enforce agent autonomy boundaries? `Hard` `30 min` [^techeon] [^reddit-expdevs-agentic]
- What are the essential components of an agent beyond an LLM? `Medium` `20 min` [^techeon] [^reddit-expdevs-agentic] [^reddit-ai-agentic]
- How do you prevent agents from over-reasoning or over-planning? `Medium` `25 min` [^techeon] [^reddit-csuk-agents] [^reddit-expdevs-agentic]
- Walk through a production-ready agent architecture. `Hard` `40 min` [^techeon] [^reddit-expdevs-agentic] [^reddit-csuk-agents]
- What logic belongs in the orchestrator vs the LLM? `Hard` `30 min` [^techeon] [^reddit-expdevs-agentic] [^reddit-aiagents-prep]
- How do you design a safe and debuggable agent loop? `Hard` `35 min` [^techeon] [^reddit-expdevs-agentic] [^reddit-csuk-agents]
- How do you implement termination conditions in long-running agents? `Medium` `25 min` [^techeon]
- How do agents decompose high-level goals into executable steps? `Medium` `25 min` [^techeon] [^reddit-csuk-agents]
- Chain-of-thought vs tree-of-thought vs graph planning - when would you use each? `Hard` `30 min` [^techeon]
- How do you detect and stop infinite planning loops? `Medium` `25 min` [^techeon] [^reddit-csuk-agents] [^reddit-expdevs-agentic]
- How do you handle partial observability or missing information? `Medium` `25 min` [^techeon] [^reddit-csuk-agents]
- How do agents decide a task is "done"? `Medium` `20 min` [^techeon]
- What planning failures are hardest to detect in production? `Hard` `30 min` [^techeon] [^reddit-expdevs-agentic]
- How do agents decide which tool to use? `Medium` `20 min` [^techeon] [^reddit-csuk-agents] [^reddit-aiagents-prep]
- How do you design tool schemas that reduce hallucinated actions? `Hard` `30 min` [^techeon] [^reddit-grilled-rag]
- How do you sandbox tool execution safely? `Medium` `25 min` [^techeon] [^reddit-expdevs-agentic]
- How do you handle tool failures, retries, and idempotency? `Medium` `25 min` [^techeon] [^reddit-expdevs-agentic] [^reddit-csuk-agents] [^reddit-aiagents-prep]
- What are the biggest security risks with tool-using agents? `Hard` `30 min` [^techeon] [^reddit-expdevs-agentic] [^datainterview-mistral]
- How do you control cost explosions from tool calls? `Medium` `25 min` [^techeon] [^reddit-expdevs-agentic] [^reddit-csuk-agents]
- Stateless vs stateful agents - tradeoffs and use cases? `Medium` `20 min` [^techeon] [^reddit-expdevs-agentic]
- How do you version and roll back agent behavior? `Medium` `20 min` [^techeon]
- Describe how you would architect an AI agent system, including the agent loop, tool interfaces, memory design, orchestration technologies, and safety considerations. `Hard` `45 min` [^igotanoffer]
- Design an agent analyzing customer support tickets, drafting responses, and escalating complex issues. `Hard` `40 min` [^promptlayer]
- Create a system where agents collaborate on research reports with citations. `Hard` `40 min` [^promptlayer]
- Build an agent reviewing code and suggesting improvements. `Hard` `35 min` [^promptlayer]
- How do you explain agentic systems to non-technical stakeholders? `Medium` `20 min` [^techeon] [^reddit-expdevs-agentic]
- What types of memory do agentic systems need? Describe working, episodic, semantic, and procedural memory. `Medium` `25 min` [^techeon] [^reddit-expdevs-agentic]
- How do you design long-term memory without polluting it? `Hard` `30 min` [^techeon]
- How do you implement human-in-the-loop (HIL) patterns and decide when to trigger human review? `Medium` `25 min` [^reddit-expdevs-agentic]
- How do you monitor and observe autonomous agent behavior in production? `Medium` `25 min` [^reddit-expdevs-agentic] [^reddit-csuk-agents]
- How do you architect agents for regulated or compliance-heavy domains (e.g., financial, healthcare)? `Hard` `35 min` [^reddit-expdevs-agentic]
- When do you use orchestration vs choreography patterns for multi-agent systems? `Hard` `30 min` [^reddit-expdevs-agentic]
- How do you filter PII in agent pipelines before data reaches the LLM? `Medium` `20 min` [^reddit-expdevs-agentic]
- How do you evaluate agent performance? What metrics matter (tool selection quality, action advancement, context adherence)? `Hard` `30 min` [^reddit-aiagents-prep]

## Fine-tuning and Training

- When would you fine-tune vs use prompt engineering? `Medium` `25 min` [^process-analysis] [^reddit-prep-ai-eng] [^reddit-genai-consulting] [^x-ashutosh-1] (reported across multiple companies)
- What is PEFT/LoRA and when would you use it? `Medium` `25 min` [^fahd-mirza] [^reddit-genai-consulting] [^x-interviewstack-meta] [^x-aryyann8] [^reddit-llm-interview-prep]
- What is QLoRA and how does it differ from LoRA? When would you choose one over the other? `Hard` `30 min` [^x-aryyann8]
- What is RLHF and why is it important? `Medium` `25 min` [^proptech-founder-1]
- Fine-tune or use prompt-engineered RAG? `Medium` `25 min` [^system-design-handbook] [^reddit-prep-ai-eng] [^hn-39748537]
- How would you design a model that can solve math problems? Walk through data collection, supervised fine-tuning, post-training, and evaluation. `Hard` `45 min` [^igotanoffer]
- How would you design a scalable and efficient system for training a large language model, considering both computational and data constraints? `Hard` `45 min` [^igotanoffer]
- Explain the RLHF pipeline: supervised fine-tuning, reward model training, and PPO. How does DPO simplify this? `Hard` `35 min` [^proptech-founder-1]
- What is instruction tuning and how does it differ from pre-training? `Medium` `20 min` [^hn-46319888] [^llmgenai] [^reddit-llm-interview-prep]
- What is speculative decoding and how does it speed up inference? `Hard` `30 min` [^sundeep-teki]
- How do you convert implicit user behavior (edits, acceptance, rejection) into training signals for model improvement? `Hard` `35 min` [^bhavishya-pandit]
- Explain quantization. What are the trade-offs between model size, speed, and accuracy? `Medium` `25 min` [^raghu-teja-2] [^reddit-llm-interview-prep]

## Evaluation and Metrics

- What metrics do you consider when benchmarking and evaluating LLM performance? `Medium` `20 min` [^proptech-founder-1]
- How do you evaluate a chatbot? `Medium` `25 min` [^process-analysis] [^reddit-clear-genai] (candidates wish they prepared for this)
- How do you detect and mitigate hallucinations in production? `Hard` `35 min` [^process-analysis] [^reddit-ai-eng-questions] [^reddit-genai-consulting] [^hn-41541053] [^hn-46873753] (reported across multiple companies)
- How would you prevent factual errors in a summarization system? `Medium` `25 min` [^interviewnode]
- How would you reduce hallucinations in a medical chatbot? `Hard` `35 min` [^interviewnode]
- What happens when the LLM is confidently wrong? How do you debug a RAG chatbot giving confident but wrong answers? `Hard` `35 min` [^process-analysis] [^datainterview-mistral] (candidates wish they prepared for this)
- Explain SHAP, LIME, and model interpretability. `Medium` `25 min` [^fahd-mirza]
- How do you detect and mitigate hallucinations? `Hard` `30 min` [^system-design-handbook]
- Explain evaluation metrics: perplexity, ROUGE, BLEU. What are the pitfalls of n-gram-based metrics? `Medium` `25 min` [^fahd-mirza] [^reddit-genai-product] [^reddit-llm-interview-prep]
- What are your testing strategies for non-deterministic outputs? `Medium` `25 min` [^reddit-prep-ai-eng]
- How do you measure accuracy in generative systems where traditional metrics don't apply? `Hard` `30 min` [^reddit-grilled-rag]
- What operational/business metrics matter for AI systems beyond accuracy? (win rate, deflection rate, p95 latency) `Medium` `25 min` [^reddit-eightfold-ai]
- How would you evaluate and monitor a model in production, not just offline? `Hard` `35 min` [^reddit-swe-to-ai]
- How have you addressed bias/fairness in your models? Can you provide an example of a trade-off you've faced? `Medium` `25 min` [^reddit-hiring-process]
- What is time to first token and why does it matter for user experience? `Easy` `15 min` [^proptech-founder-1]
- How do you measure hallucination rate in production? `Hard` `30 min` [^buildml] [^llmgenai] [^hn-46959695] [^hn-42313401]
- What is "vibes-based" evaluation vs. a formal eval framework? How do you build proper evals? `Medium` `25 min` [^exponent-openai]
- How do you build a golden dataset for evaluation? How do you use it for regression testing? `Hard` `35 min` [^proptech-founder-1]
- How does the system get better over time? Describe feedback and reinforcement loops. `Medium` `25 min` [^interviewnode]
- How do you decide success metrics for an ML model? `Medium` `20 min` [^raghu-teja-2]
- How would you implement A/B testing for different prompt variations? `Medium` `25 min` [^hn-44875256]
- How would you test a new model before full deployment? Describe A/B testing, canary, interleaved, and shadow testing strategies. `Hard` `35 min` [^x-akshay-pachaar-1]
- Two models have identical accuracy but different confidence levels. Which do you choose? Explain model calibration. `Hard` `30 min` [^x-akshay-pachaar-3]
- A production chatbot's accuracy dropped from 95% to 80% in six weeks. How do you diagnose the root cause before retraining? `Hard` `35 min` [^x-ashutosh-2]

## ML Fundamentals

- How do you approach data pre-processing and feature engineering? `Easy` `15 min` [^fahd-mirza]
- Explain SQL versus NoSQL databases for AI workloads. `Easy` `15 min` [^fahd-mirza]
- What steps would you take to diagnose performance bugs in a model? `Medium` `20 min` [^fahd-mirza]
- Should you optimize for latency or throughput? (for a personal assistant with one request) `Medium` `20 min` [^youtube-short]
- Should you use data parallelism for a single-request personal assistant? Why or why not? `Medium` `20 min` [^youtube-short]
- Explain how Transformers work. Why are they foundational? `Medium` `25 min` [^process-analysis] [^reddit-genai-consulting] (reported across multiple companies)
- How would you handle real-time versus batch processing for data updates? When is one preferred over the other? `Medium` `20 min` [^proptech-founder-2]
- How do you ingest and process different types of data (structured, unstructured, event data)? `Medium` `20 min` [^proptech-founder-2]
- Explain the bias-variance tradeoff in simple terms. `Easy` `15 min` [^reddit-swe-to-ai]
- Why are neural networks usually not the first choice for tabular data? `Easy` `15 min` [^reddit-swe-to-ai]
- How do you handle imbalanced datasets in real projects? `Medium` `20 min` [^reddit-swe-to-ai] [^reddit-hiring-process] [^raghu-teja-2]
- Explain the difference between RNN and LSTM. `Medium` `20 min` [^raghu-teja-2]
- Debug a model that runs but doesn't learn. Identify broadcasting errors and dimension mismatches. `Hard` `35 min` [^sundeep-teki]
- Statistics questions: probability, distributions, regression, Bayesian analysis, hypothesis testing. `Medium` `30 min` [^mimansa-jaiswal]
- Explain supervised vs. unsupervised learning. When would you use each? `Easy` `15 min` [^hn-29876742] [^tidorp]
- What is regularization? Compare L1, L2, and dropout. `Medium` `20 min` [^hn-29876742] [^tidorp]
- What is feature scaling and when is it necessary? Compare normalization vs standardization. `Easy` `15 min` [^x-aryyann8]
- Implement cosine similarity in NumPy. `Easy` `15 min` [^reddit-amazon-genai]

## Python and Software Engineering

- How do you handle race conditions in your code? `Medium` `20 min` [^proptech-founder-2]
- What is the Global Interpreter Lock (GIL) in Python? `Easy` `15 min` [^proptech-founder-2]
- What is something unique about Python when it comes to concurrency? `Easy` `15 min` [^proptech-founder-2]
- What are some problems you can run into when using asynchronous programming in Python? `Medium` `20 min` [^proptech-founder-2]
- What is Docker? `Easy` `10 min` [^khushal-kumar]
- Why do we use Selenium? `Easy` `10 min` [^khushal-kumar]
- Have you heard about Redis? `Easy` `10 min` [^khushal-kumar]
- Explain the JavaScript event loop. `Medium` `20 min` [^proptech-founder-1]
- How do you call models via API/SDK? How do you handle retries, timeouts, and logging? `Medium` `20 min` [^reddit-genai-consulting]
- Which AI development platforms or tools do you regularly use, and why? `Easy` `15 min` [^reddit-hiring-process]
- Explain memory leaks and garbage collection in Python. `Medium` `20 min` [^raghu-teja-1]
- What is the difference between class methods and static methods? `Easy` `15 min` [^raghu-teja-1]
- Explain super() and Method Resolution Order in multiple inheritance. `Medium` `20 min` [^raghu-teja-1]
- How do you debug Python code in production? "In production, there will be no VS Code." `Medium` `25 min` [^raghu-teja-1]
- How do you use asyncio for concurrent I/O in Python? When would you use threading vs. multiprocessing instead? `Medium` `25 min` [^proptech-founder-1]
- How do you optimize SQL queries? Explain the order of execution in SQL. `Medium` `20 min` [^raghu-teja-1]
- What are Git branching strategies for deployment? How do you perform a rebase? How do you handle merge conflicts? `Medium` `20 min` [^raghu-teja-1]
- Have you worked with real-time communication technologies like WebRTC? `Medium` `20 min` [^fahd-mirza-2]

## Infrastructure and MLOps

- How would you design a large-scale AI model deployment system? `Hard` `45 min` [^designgurus]
- How would you design a distributed training system for deep learning? `Hard` `45 min` [^designgurus] [^x-akshay-pachaar-2]
- How would you design a scalable data pipeline for ML applications? `Hard` `40 min` [^designgurus]
- How would you design a GenAI system to handle traffic spikes without overwhelming the model provider? `Hard` `40 min` [^igotanoffer]
- How would you monitor production AI systems? `Medium` `25 min` [^system-design-handbook]
- What are major scaling challenges for LLM-powered applications? `Medium` `25 min` [^system-design-handbook]

## Cost and Latency Optimization

- Your app gets 1M queries/day - how do you optimize cost? `Hard` `35 min` [^process-analysis] (reported across multiple companies)
- How do you reduce token costs at scale? `Hard` `35 min` [^process-analysis] [^reddit-prep-ai-eng] [^hn-46229585] [^hn-46695170] (candidates wish they prepared for this)
- How would you think about cost and capacity planning for an LLM-powered application at scale? `Hard` `40 min` [^igotanoffer]
- How would you make GPT-based API calls cost-efficient under heavy load? `Hard` `35 min` [^interviewnode]
- How would you reduce token costs? `Medium` `25 min` [^system-design-handbook]
- Explain quantization and model distillation for inference optimization. `Hard` `30 min` [^fahd-mirza]
- Describe the latency/cost/relevancy tradeoff triangle in GenAI systems. How do you manage all three? `Hard` `35 min` [^proptech-founder-2]
- How do you reduce latency in GenAI applications? `Medium` `25 min` [^proptech-founder-2]
- Cost vs. quality trade-offs: when is a small open-source model "good enough" vs. GPT-4-class? `Medium` `25 min` [^reddit-genai-consulting]
- By trimming prompts and caching embeddings, how would you reduce API spend? Walk through a before-and-after cost breakdown. `Hard` `35 min` [^fonzi-ai]
- Explain multi-layer caching strategies: retrieval cache, prompt cache, and response cache. `Medium` `25 min` [^interviewnode]
- What is model tiering? When do you route to a small distilled model vs. a large LLM? `Medium` `25 min` [^interviewnode] [^hn-42793253] [^hn-47150302]
- What is prompt compression and how does it reduce cost? `Medium` `20 min` [^llmgenai] [^hn-46319888] [^hn-44013971]
- Latency vs. throughput optimization for LLM serving - what are the trade-offs? `Hard` `30 min` [^youtube-short]
- How would you benchmark each LLM call in a multi-step pipeline to identify latency bottlenecks? `Medium` `25 min` [^proptech-founder-1]
- Estimate the budget for a RAG pipeline at enterprise scale (e.g., 300,000 legal contracts). `Hard` `35 min` [^reddit-devsindia-genai]
- What's the real bottleneck in LLM serving throughput? How does PagedAttention address it? `Hard` `35 min` [^x-athletickoder-1]

## Safety and Guardrails

- When and how would you implement LLM guardrails? `Medium` `25 min` [^proptech-founder-1]
- How would you design a language model that minimizes harmful outputs while still being useful and expressive? `Hard` `40 min` [^igotanoffer]
- How would you build a system that detects whether content violates policy or contains offensive material? `Hard` `40 min` [^igotanoffer]
- How do you protect against prompt injection and jailbreaking? `Hard` `35 min` [^system-design-handbook] [^reddit-ai-eng-questions] [^reddit-expdevs-agentic] [^hn-44268335]
- What steps would you take to handle exceptions in a GenAI application? `Medium` `20 min` [^proptech-founder-2]
- Explain Constitutional AI and alignment considerations. `Hard` `30 min` [^sundeep-teki]
- How do you handle data privacy and PII in prompts and logs? `Medium` `25 min` [^reddit-genai-consulting] [^reddit-expdevs-agentic]
- How do you address bias in training data and generated content? `Medium` `25 min` [^reddit-genai-consulting] [^reddit-hiring-process]
- How do you red-team an LLM system? `Hard` `35 min` [^sundeep-teki]
- Your application generates code that gets executed. How do you prevent malicious code generation and execution? `Hard` `40 min` [^proptech-founder-1]

---

## Recommended Reading

- [The 0-to-1 AI Engineer Interview Playbook](https://valenx.org/books/aie) — Covers LLM system design, RAG, agents, evaluation, and behavioral questions. The most comprehensive single resource for AI engineering interview preparation.
- [The 0-to-1 ML Engineer Interview Playbook](https://valenx.org/books/aie) — Production ML systems, model training, MLE system design. Essential for roles that blend classical ML with modern LLM engineering.
