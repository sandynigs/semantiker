# 🧠 semantiker: Local LLM Semantic Caching Utility

## Overview

`semantiker` is a lightweight Python utility designed to introduce a high-performance semantic caching layer between your application and a local Large Language Model (LLM) server. Its primary goal is to minimize redundant LLM calls by leveraging vector embeddings to check for semantically similar historical queries.

This utility is essential for developers building cost-effective, real-time applications using local inference, as it drastically reduces latency and computational load.

## ✨ Features: Problem Solved

The `semantiker` package addresses the core issue of **costly and slow repetition** inherent in working with LLMs by providing:

1.  **Semantic Cache Hitting:** Uses vector similarity checks (cosine similarity) to match new queries against the cache, ensuring relevant hits even when the input phrasing is different.
2.  **Latency Reduction:** By serving similar queries from the cache, response times drop from seconds (LLM inference) to milliseconds (vector lookup).
3.  **Ollama Integration:** Seamlessly works with the Ollama API, allowing for rapid deployment using popular local models like Mistral, Llama 2, or Code Llama.
4.  **Configurable Threshold:** Allows developers to fine-tune the strictness of the cache matching to balance performance gains against answer relevance.

## ⚙️ Prerequisites

To test and run the application, you **must** have a local LLM environment configured:

| **Component** | **Requirement** | **Setup Command** | 
| :--- | :--- | :--- |
| **Python** | Version 3.8+ | N/A | 
| **Ollama** | Must be installed and running locally. | [Download Ollama] | 
| **LLM Model** | A model must be pulled and available in Ollama. | `ollama pull mistral` | 

## 📦 Installation

To install the core package along with the dependencies required to run the included FastAPI test application:

```bash
# 1. Install the core library
pip install semantiker

# 2. Install dependencies for the FastAPI Test Application
pip install fastapi uvicorn pydantic


## 🛑 Current Limitations (V1.0)

While the core functionality is robust, the current version of `semantiker` maintains a focused scope.

1.  **Client Dependency:** Currently, only the **Ollama API** is supported via the `OllamaClient`.
2.  **Vector Storage:** The system relies exclusively on an **in-memory FAISS index** for vector storage, meaning the cache is reset every time the application restarts.
3.  **Cache Type:** Only supports **in-memory dictionaries** for storing the LLM responses.

## 🛠️ Architectural Design for Extensibility

The core strength of `semantiker` lies in its modular design, which is specifically built to overcome the V1.0 limitations easily. This clean separation of concerns provides immediate **provisions for future support** of external services and custom components:

* **Decoupled Clients:** The `LLMClient` (for LLM communication) is separated from the `SemanticCacheUtility` (for caching logic). This provision allows new client classes (e.g., `OpenAIClient`, `GeminiClient`) to be added by simply implementing the abstract client interface.
* **Pluggable Storage:** The current in-memory FAISS and Python dictionaries can be easily swapped out for persistent solutions. Abstract storage interfaces can be introduced for vector indexes and key-value stores, allowing seamless integration with **Chroma, Pinecone, or Redis**.
* **Custom Embeddings:** The architecture is set up to allow the user to provide a custom Sentence Transformer model, decoupling the embedding generation from the LLM provider.

## 🚀 Testing the Application

To test the semantic caching in action, use the provided FastAPI example application:

1.  **Navigate** to the test directory:

    ```bash
    cd test-fast-api-app
    ```

2.  **Run** the server (ensure Ollama is running first):

    ```bash
    uvicorn main:app --reload
    ```

    The API documentation will be available at `http://localhost:8000/docs`.

3.  **Test the API** by sending two queries that are semantically similar but phrased differently (e.g., "best rain cloud" and "cloud producing most precipitation") and observe the difference in latency to confirm the cache hit.

## 🔮 Future Extensions

| **Improvement** | **Scope and How to Achieve It** | 
| :--- | :--- |
| **Persistence Layer** | **Scope:** Maintain cache integrity across application restarts and scale horizontally. **How:** Implement abstract `CacheStorage` interfaces and create concrete implementations for external storage like **Redis** (for key-value) and dedicated vector databases. | 
| **External API Clients** | **Scope:** Enable seamless deployment to major cloud services. **How:** Create dedicated client classes (e.g., `OpenAIClient`, `GeminiClient`) implementing the unified `AbstractLLMClient` interface. | 
| **Custom Embedding Models** | **Scope:** Decouple embedding generation from the Ollama LLM call for fine-grained control and performance. **How:** Integrate the `Sentence Transformers` library and allow configuration of local embedding models within the `SemanticCacheUtility`. | 
| **Time-to-Live (TTL)** | **Scope:** Prevent the application from returning stale information. **How:** Implement cache expiration logic to check timestamps on cached entries and automatically force a cache miss if the entry is older than a configurable `ttl_seconds`. |
