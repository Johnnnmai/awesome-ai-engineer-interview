# AI System Design Interview Questions

Consolidated from 100+ sources including blog posts, YouTube transcripts, Reddit threads, Medium articles, and interview guides. Every question was extracted from actual interview experiences or preparation materials.

## AI System Design

- Design ChatGPT. [^igotanoffer]
- Design our Claude chat service. [^igotanoffer]
- Design a small language learning model that could run on a phone while making sure it's polite. [^igotanoffer]
- Here's a junior developer's design for an inference batching system. Can you review it and explain what you'd change or improve? [^igotanoffer]
- Design the OpenAI Playground - specifically the feature that lets developers simulate full conversations and threads. [^exponent-openai]
- Design a real-time chatbot API (low-latency handling, session management, concurrency, safety filters). [^designgurus]
- Design a Document Q&A Assistant. [^bhavishya-pandit]
- Design a Hallucination-Free Banking Chatbot. [^bhavishya-pandit]
- Design a Hospital Voice Assistant (handle noise, privacy, latency, domain vocabulary). [^bhavishya-pandit]
- Design a Feedback Loop for Writing Tools. [^bhavishya-pandit]
- Design a Legal Contract Generation system with compliance requirements. [^bhavishya-pandit]
- Design an AI Search system scaling to 10M+ articles. [^bhavishya-pandit]
- Design a Resume Classifier for Team Routing. [^bhavishya-pandit]
- Design an AI-powered Candidate Sourcing System with 750M profiles, semantic search, and <500ms latency. [^colin-zhou]
- Scale an AI chat feature to 1M daily users - discuss trade-offs. [^process-analysis] (reported across multiple companies)
- Design for 1M users (scale beyond prototype). [^process-analysis] (candidates wish they prepared for this)
- Design a system to process 10k user uploads per month (bank payslips, IDs, references). How would you extract data, detect inconsistencies, reject invalid files, and handle LLM provider downtime? [^igotanoffer]
- Design a system that lets doctors automatically send billing info to insurers based on patient notes. [^igotanoffer]
- Design a conversational recommender system that suggests products based on user preferences, combining chat, retrieval, and database layers. [^igotanoffer]
- Design a fast autocomplete system using LLMs. [^system-design-handbook]
- Design an AI-powered legal assistant. [^system-design-handbook]
- Build a generative resume builder with memory. [^system-design-handbook]
- Create an internal Slack bot answering HR questions. [^system-design-handbook]
- Design a GitHub Copilot-style JavaScript development tool. [^system-design-handbook]
- Design an AI co-pilot like GitHub Copilot (real-time streaming completions). [^colin-zhou]
- Design a Midjourney/Stable Diffusion image generation service (queueing, GPU scheduling). [^colin-zhou]
- Design a Perplexity.ai / real-time LLM-powered search engine. [^colin-zhou]
- Design a Ghibli Image Generator (text prompt ingestion, model selection, GPU inference, cost throttling, safety filters). [^rohit-verma]
- Design a Dynamic Questionnaire Engine for an Insurance Platform (JSON-driven, frontend decision tree without backend calls). [^rohit-verma]
- Design a user profile system addressing storage, multi-device tracking, and preference flexibility. Optimize for 100 million users with batch migration. [^linkjob-openai]
- Design a distributed search system capable of handling a billion documents and a million QPS, while also managing LLM inference for over 10,000 requests per second. [^linkjob-anthropic]
- Design hybrid search combining traditional text retrieval with semantic similarity - top-k similar documents from a corpus of over 10M documents with a response time under 50ms. [^linkjob-anthropic]
- Design a workflow to remove all dead links for hundreds of client websites assuming you have API access to overwrite their HTML. [^proptech-founder-2]
- How would you design the UX for an AI assistant that is often slow? [^igotanoffer]
- How would you surface model limitations or errors to users without breaking trust? [^igotanoffer]
- Design a scalable image-generation pipeline for millions of users. [^interviewnode]
- How would you scale a generative content platform for millions of users? [^interviewnode]
- Design an In-Memory Database with SET, GET, BEGIN, ROLLBACK, COMMIT, and nested transaction support. [^devto-xai]
- Design an AI recommendation system. [^reddit-swe-to-ai]
- Design a fraud detection system. [^reddit-swe-to-ai]
- Design a chatbot architecture end-to-end (LLM + backend + data flow). [^reddit-swe-to-ai]
- Design a distributed job queue for 100k+ GPU training jobs with preemption and checkpointing. [^reddit-xai-eng]
- Design a temperature prediction system handling inconsistent global datasets (hybrid ML-LLM). [^reddit-grilled-rag]
- Design an end-to-end RAG service: data ingestion, indexing, retrieval, generation, evals, tracing, guardrails. [^reddit-eightfold-ai]
- Design a rate-limiter and code the core part. [^reddit-xai-eng]
- Scaling AI systems to millions of users: latency and cost trade-offs, batching, caching, streaming, failure modes. [^reddit-2026-prep]
- Design ChatGPT's cross-conversation memory feature. [^igotanoffer]
- Design a multi-step agentic workflow (meeting scheduling, code review, email campaigns). [^promptlayer]
- Design a content/policy violation detection system. [^igotanoffer]
- Design a unified query engine across dispersed data sources like email, calendar, documents, and chat. [^x-avi-chawla-1]
- How would you implement an AI application from start to finish, from kickoff meeting through deployment? (IBM) [^raghu-teja-2]
- How would you design a scalable and reliable automation workflow? What considerations for error handling, monitoring, and debugging? [^proptech-founder-1]
- How would you handle real-time versus batch processing for data updates? When is one preferred over the other? [^proptech-founder-2]
- How do you ingest and process different types of data (structured, unstructured, event data)? [^proptech-founder-1]

## Traditional System Design

- Design GitHub Actions. [^hello-interview]
- Design Slack. [^hello-interview]
- Design Online Chess. [^hello-interview]
- Design a Payment System. [^hello-interview]
- Design a Webhook Callback System. [^hello-interview]
- Design TinyURL (Bitly). [^colin-zhou]
- Design Instagram / TikTok feed. [^colin-zhou]
- Design Twitter / X (timeline, posting, followers, trending topics). [^colin-zhou]
- Design YouTube / Netflix video streaming platform. [^colin-zhou]
- Design Uber (ride-sharing backend: matching, ETA, pricing surges). [^colin-zhou]
- Design WhatsApp / Messenger (1:1 + group chat at global scale). [^colin-zhou]
- Design a distributed key-value store (like DynamoDB / Cassandra). [^colin-zhou]
- Design Google Docs collaborative editing (real-time, eventually consistent). [^colin-zhou]
- Design Yelp / Google Maps nearby search. [^colin-zhou]
- Design a rate limiter (global, per-user, distributed). [^colin-zhou]
- Design Discord (voice + text chat, millions concurrent in voice channels). [^colin-zhou]
- Design Stripe payment processing system (high consistency, PCI compliance). [^colin-zhou]
- Design a distributed job scheduler (like AWS Batch at planetary scale). [^colin-zhou]
- Design a notification system that can send 1B notifications/day with <1% loss. [^colin-zhou]
- Design a strongly-consistent distributed database (Spanner / CockroachDB-like). [^colin-zhou]
- Design a high-frequency trading exchange matching engine. [^colin-zhou]
- Our p99 latency went from 50ms to 2s overnight - how would you debug and fix? [^colin-zhou]
- Design a global WebSocket service (10M+ concurrent connections). [^colin-zhou]
- Design a global feature flag / config service (multi-region, zero-downtime rollouts). [^colin-zhou]

## System Troubleshooting

- A system's 95th percentile latency spiked from 100ms to 2000ms. Identify bottlenecks rapidly. [^linkjob-anthropic]
- How would you handle a 10x traffic spike during a product launch? [^hello-interview]
- What happens if your primary data center goes offline for six hours? [^hello-interview]

---

## Further Reading

- [The 0-to-1 AI Engineer Interview Playbook](https://valenx.org/books/aie) — Dedicated chapters on LLM system design and RAG architecture cover every pattern in this question list, with worked examples and evaluation frameworks used at top AI companies.
