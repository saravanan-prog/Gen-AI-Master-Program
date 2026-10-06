from pathlib import Path

content = r'''# Module 5: Basics of Retrieval-Augmented Generation (RAG)

## 1. Introduction to RAG

### What is RAG?

RAG means:

**Retrieval-Augmented Generation**

Simple meaning:

> RAG gives useful outside information to an LLM before it creates an answer.

### Why do we need RAG?

An LLM has knowledge from its training data.

But it may not know:

- Your company documents
- Your college notes
- A new PDF
- Your private data
- Today's internal information

Example:

```text
Student asks:
"What is our college leave policy?"