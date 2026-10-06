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