# Master Program in Generative AI — Complete Syllabus

---

## Module 1: Introduction of GenAI
* **Overview of Generative AI**
* **Evolution of AI:** From rule-based to generative models
* **Key Concepts:** LLMs, diffusion models, multimodal AI
* **Real-World Applications:** Healthcare, education, marketing, finance, and enterprise use cases
* **Career Paths:** Roles and opportunities in Generative AI

---

## Module 2: Prompt Engineering using ChatGPT & Gemini
* **Fundamentals of Prompt Creation:**
  * Anatomy of a prompt (instructions, context, constraints)
  * Prompt elements (roles, input, output format)
  * Zero-shot, one-shot, and few-shot prompting
  * Structured vs. unstructured prompts
* **Techniques for Effective Prompts:**
  * Chain-of-Thought (CoT) prompting
  * Role prompting & persona-based prompts
  * Tree of Thoughts (ToT)
  * Directional stimulus prompting
* **Prompt Tuning for AI Models:**
  * System vs. user prompts
  * Refining prompts for accuracy, creativity, and consistency
  * Evaluating prompt effectiveness
* **Case Studies and Hands-On:**
  * **Business Use Cases:** Email writing, marketing copy, brainstorming
  * **Creative Use Cases:** Storytelling, poetry, art descriptions
  * **Code Generation Use Cases**
  * **Exercises:** Zero vs. few-shot comparison, role-based Chatbot, prompt chaining workflow

---

## Module 3: Python for GenAI
* **Introduction to Python & Setup:**
  * Importance of Python in Generative AI
  * Installing Python / Google Colab & Jupyter Notebook setup
  * Basic IDE navigation
* **Python Fundamentals:**
  * Variables and data types (string, integer, float, boolean)
  * Basic operators (`+`, `-`, `*`, `/`, `%`, `//`, `**`)
  * Input and output (`print()`, `input()`)
* **Working with Data:**
  * Data structures: Lists, tuples, dictionaries, sets
  * Indexing and slicing
  * Adding, updating, and removing data
  * Looping constructs (`for`, `while`)
  * List comprehensions
* **Functions & Modular Code:**
  * Defining functions (`def`)
  * Function parameters and return values
  * Built-in vs. custom functions
  * Importing Python modules
* **Working with Files:**
  * Reading and writing text files
  * JSON fundamentals for API data exchange
  * Loading & saving datasets
* **API Interaction:**
  * Introduction to APIs in Python
  * Using the `requests` library to call external APIs
  * Sending parameters and receiving responses
  * Parsing JSON responses
* **Working with Libraries for GenAI:**
  * Essential libraries: `openai`, `pandas`, `numpy`, `json`
  * Hands-on examples of calling GenAI model APIs
* **Module Project:** Create a script that:
  * Reads a prompt from a local file
  * Sends it to a GenAI API (ChatGPT / Gemini / Claude)
  * Saves the generated response to an output file
  * Analysis of results, best practices, and real-world workflow integration

---

## Module 4: Large Language Models (LLMs) - Architecture, APIs, and Deployment
* **Introduction to LLMs:**
  * What are LLMs and why they matter
  * Overview of models: GPT, Gemini, LLaMA, Mistral
* **Architecture & Key Concepts:**
  * Architecture overview of GPT, Gemini, and LLaMA
  * Tokens, context window length, inference latency, model scale
  * Strengths and limitations of major model families
* **Deployment Approaches:**
  * On-Premise vs. Cloud LLM deployment
  * Trade-offs, hardware considerations, and cost factors
* **Hands-On with APIs:**
  * OpenAI ChatGPT API (text generation, embeddings)
  * Google Gemini API (multimodal processing)
  * Meta LLaMA API (open-source customization)
  * Running local/on-premise LLMs (LLaMA, Mistral)
* **Parameter Tuning & Customization:**
  * Fine-tuning vs. Parameter-Efficient Fine-Tuning (LoRA, PEFT, Adapters)
  * Prompt-tuning vs. Instruction-tuning
  * Safety alignment & Reinforcement Learning from Human Feedback (RLHF)
  * Best practices for domain-specific performance optimization
* **Ethical Considerations:**
  * Hallucination risk mitigation
  * Bias detection and fairness
  * Data privacy, compliance, and governance
* **Module Project:** Build a Domain-Specific LLM Intelligent Assistant (Select one):
  * **Education Assistant:** Answers student queries, generates study plans, and summarizes lessons.
  * **Customer Support Chatbot:** Handles FAQs, routes complex tickets, and generates summary reports.
  * **Business Knowledge Assistant:** Queries internal data, generates sales pitches, and creates executive summaries.
  * **Creative Writing Assistant:** Brainstorms story concepts, drafts marketing copy, and writes poetry.
  * **Healthcare Q&A:** Responds to medical FAQs with disclaimers and summarizes clinical literature.

---

## Module 5: Basics of Retrieval-Augmented Generation (RAG)
* **Introduction to RAG:**
  * Why LLMs require external knowledge bases
  * How RAG mitigates hallucinations
  * Industry use cases and applications
* **Embeddings Basics:**
  * Vector representation of text semantics
  * Semantic similarity concepts and distance metrics
  * Role of embedding models in retrieval pipelines
* **Chunking & Document Preparation:**
  * Document parsing and splitting techniques
  * Optimal chunk size selection and chunk overlap
  * Text cleaning and preprocessing strategies
* **Vector Databases:**
  * Purpose and necessity over traditional SQL/NoSQL databases
  * Hands-on experience with ChromaDB
* **Retrieval Methods:**
  * Cosine similarity search
  * Maximal Marginal Relevance (MMR) for diversity
  * Hybrid search (keyword + vector search)
* **RAG Pipeline Architecture:**
  * Workflow: $Query \rightarrow Embedding \rightarrow Search \rightarrow Context \rightarrow Response$
  * Impact of retrieved context quality on model output
* **No-Code / Low-Code RAG Implementation:**
  * Ingesting documents using LlamaIndex / Lamini
  * Automated embedding generation and retrieval verification
* **Best Practices & Pitfalls:**
  * Document hygiene, chunk tuning, model selection, noise filtering

---

## Module 6: Advanced AI Agents & RAG using LangChain
* **Introduction to LangChain & Core Concepts:**
  * LangChain architecture and ecosystem overview
  * Core primitives: Chains, Agents, Tools, Memory, Prompt Templates
  * Supporting multi-step reasoning and retrieval pipelines
  * Environment setup, API key management, and SDK configuration
  * Constructing basic chains and executing prompts
* **Building RAG Pipelines in LangChain:**
  * Ingesting data into LangChain retrievers
  * Chunking strategies & embedding generation
  * Vector store integration
  * Building end-to-end retrieval chains
  * Context injection and performance optimization
* **Building Advanced AI Agents in LangChain:**
  * Understanding agent reasoning frameworks (Zero-shot, ReAct, multi-step)
  * Integrating conversational memory for context retention
  * Connecting tools and external APIs to agents
  * Multi-step autonomous agent workflows
* **Module Project:** LangChain AI Agent with RAG
  * **Objective:** Build a domain-specific AI assistant with multi-step reasoning, memory, and retrieval capacities.
  * **Implementation Steps:** Problem definition, retriever construction, agent setup with tool integrations (web scraping, external APIs), performance tuning, and delivery.

---

## Module 7: Building Stateful AI Workflows using LangGraph
* Introduction to LangGraph and graph-based architectures
* State management and persistence in complex AI tasks
* Human-in-the-Loop (HITL) system designs
* Multi-step workflow construction
* Agent orchestration patterns
* Advanced workflow design principles
* **Module Project:** Graph-based stateful agent system

---

## Module 8: Multi-Agent Systems using CrewAI / AutoGen
* Fundamentals of agent collaboration and multi-agent systems
* Role-playing definitions, goals, and backstories
* Task assignment and dynamic task delegation
* Agent-to-agent communication protocols
* Autonomous task execution workflows
* Designing scalable multi-agent architectures
* Hands-on implementation using CrewAI and AutoGen
* **Module Project:** Collaborative multi-agent workflow solution

---

## Module 9: Introduction to Model Context Protocol (MCP)
* **Introduction to MCP:**
  * What is Model Context Protocol (MCP)?
  * Importance of standardizing LLM-to-tool connections
  * How MCP integrates models with tools, databases, and APIs
* **MCP Architecture:**
  * Client, Server, and Host relationships
  * Communication protocols and flow
  * Secure external resource access mechanics
* **MCP Tools & Resources:**
  * Invoking local and remote tools via MCP
  * File system, database, API, and browser access
  * Permission models and resource handling
* **MCP Workflow Basics:**
  * Request-response lifecycles
  * Structured tool-calling execution
  * Context sharing across applications
* **MCP Use Cases:**
  * Augmenting AI assistants with desktop tools
  * IDE integrations and coding workflow automation
  * Enterprise data pipelines
* **Hands-On Setup & Application Building:**
  * Installing MCP servers and setting up configurations
  * Building a custom MCP server from scratch
  * Exposing tools to LLMs and testing execution
* **Security, Best Practices, & Future Outlook:**
  * Granular access control, sensitive data handling, reducing tool exposure
  * Evolution of MCP in enterprise ecosystems and autonomous agent networks

---

## Module 10: Vibe Coding (GitHub Copilot / Claude / Codex)
* **Introduction to Vibe Coding:**
  * Concept of "Vibe Coding" and AI-first software development
  * Evolution of developer tooling and IDE assistants
  * Tool suite overview: GitHub Copilot, Claude, Codex, Gemini
* **AI-Powered Code Generation:**
  * Effective prompt design for precise code generation
  * Generating CRUD modules, API endpoints, backend scripts, and frontend components
  * Scaffold generation using reusable templates and boilerplates
* **Code Explanation & Reverse Engineering:**
  * Natural language code walkthroughs for complex functions
  * System architecture and design pattern analysis
  * Identifying code smells and automated refactoring
  * Onboarding to legacy codebases using AI assistance
* **Debugging & Code Optimization:**
  * Analyzing stack traces, compilation, and runtime error resolution
  * Performance tuning, query optimization, and memory management
* **Future of AI-Assisted Engineering:**
  * Rapid prototyping, autonomous coding agents, and modern dev stacks

---

## Module 11: Vibe Coding using Emergent
* **Emergent Platform Mastery:**
  * Platform environment setup and navigation
  * Core engine mechanics and developer intent interpretation
* **Rapid Prototype Development:**
  * Generating complete application scaffolds from single prompts
  * Iterative UI/UX customization through conversational feedback
* **Multi-Agent Orchestration:**
  * Coordinating specialized agents for frontend, backend, and logic layer generation
  * Visual artifact review and real-time previews
* **Production Workflows:**
  * Translating prototype concepts to production-ready codebases
  * Integrating Emergent outputs with local development environments and CI/CD pipelines

---

## Module 12: Vibe Coding using Google Antigravity
* **Agent-First Architecture:**
  * Evolution from traditional IDEs to autonomous agent orchestration
  * Principles governing agent-driven development environments
* **Antigravity Environment Setup:**
  * VS Code Fork setup and interface navigation
  * Managerial view, Mission Control, and task spawning
  * Writing goal-driven developer prompts
* **Multi-Agent Coordination & Practice:**
  * Executing end-to-end software builds from high-level goals
  * Iterative UI adjustments, code refactoring, automated bug finding, and unit test generation

---

## Module 13: Building Advanced AI Agents using n8n
* **Introduction to n8n:**
  * Platform overview, benefits, and contrast with tools like Zapier
  * Core concepts: Workflows, nodes, triggers, actions, credentials
* **Environment Setup & Navigation:**
  * Cloud vs. Self-Hosted n8n setup
  * Navigating the canvas editor
  * Understanding node categories (Trigger, Action, Function, Code)
* **Workflow Construction:**
  * Creating triggers (Webhook, Manual, Schedule)
  * Integrating API actions and handling data structures
  * Variable usage, expressions, conditional logic, error handling, retries, and looping
* **Service Integrations & Automation:**
  * Connecting cloud services (Google Sheets, Gmail, Airtable, Notion)
  * Authenticating custom API endpoints securely
  * Building business automation pipelines (CRM, email triggers, reporting)
* **Module Project:**
  * Building an automated lead generation engine, document knowledge assistant, or social media pipeline.
  * Workflow structure, credentials management, version control, and monitoring best practices.

---

## Module 14: Cloud Deployment for Generative AI (AWS / GCP)
* **AWS Generative AI Ecosystem:**
  * Overview of AWS GenAI capabilities
  * Amazon Bedrock & Foundation Model selection
  * Hands-on with Bedrock Playground
  * Amazon SageMaker basics: Deploying, scaling, and monitoring pre-trained models
* **Google Cloud Platform (GCP) GenAI Ecosystem:**
  * Overview of GCP GenAI services
  * Vertex AI Studio & Gemini Model integration
  * Utilizing Model Garden
  * Model deployment, endpoint testing, operational monitoring, and cost optimization

---

## Final Capstone: AI Hackathon
* **Comprehensive Project:** Design, build, and deploy an end-to-end, production-ready Generative AI application.
* **Requirements:** Utilize modern orchestration frameworks (LangChain/LangGraph/CrewAI), cloud infrastructure (AWS/GCP), stateful automation (n8n/MCP), and AI tools to solve a real-world enterprise problem.