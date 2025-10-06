# 🧠 semantiker: Local LLM Semantic Caching Utility

## Overview

`semantiker` is a lightweight Python utility designed to introduce a high-performance semantic caching layer between your application and a local Large Language Model (LLM) server, such as **Ollama**.

By leveraging vector embeddings, the utility quickly checks if a semantically similar query has been asked before. This prevents redundant calls to the LLM, drastically reducing latency, computational load, and API costs (if transitioning to cloud-based APIs later).

This solution is engineered specifically for developers using local inference engines to build cost-effective, real-time applications.

***

## ✨ Capabilities (Features)

* **Semantic Cache Hitting:** Uses vector similarity to match new queries against historical results, offering highly relevant cache hits even if the query phrasing is different.

* **Ollama Integration:** Seamlessly integrates with the Ollama API, allowing rapid deployment with powerful local models like Mistral, Llama 2, or Code Llama.

* **Performance Metrics:** Automatically logs whether a response was a cache hit or required a fresh LLM generation (Cache Miss).

* **Configurable Threshold:** Allows the user to set a custom cosine similarity threshold to fine-tune the strictness of the cache matching.

* **Clean Architecture:** Separates the LLM Client logic (`OllamaClient`) from the core Caching utility (`SemanticCacheUtility`).

***

## ⚙️ Prerequisites

This package **is not a standalone utility**. It requires a local LLM inference engine to be installed and running.

| **Component** | **Requirement** | **Setup Command** | 
 | ----- | ----- | ----- | 
| **Python** | Version 3.8+ | N/A | 
| **Ollama** | Must be installed and running locally. | [Download Ollama](https://ollama.com) | 
| **LLM Model** | A model must be pulled and available in Ollama. | `ollama pull mistral` | 

**Crucial Note:** The Ollama server must be running **before** you start any application that uses the `semantiker` package.

***

## 📦 Installation

1.  **Install the package:**

    ```bash
    pip3 install semantiker
    ```

2.  **Install dependencies for the Test Application (FastAPI):**

    ```bash
    pip3 install fastapi uvicorn pydantic
    ```

***

## 🚀 Usage Example: FastAPI Cache Tester

A functional test application is provided in the `test-fast-api-app` directory to demonstrate semantic caching and latency reduction in a real-world scenario.

### 1. Run the Test Application

Navigate to the test directory and run the main file (assuming you have installed the required dependencies, including `uvicorn`, as detailed above):
Test results can be found inside docs folder.

```bash
cd test-fast-api-app
uvicorn main:app --reload
