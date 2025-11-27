# 🇵🇰 Constitutional Q&A System — Retrieval-Augmented Generation (RAG)

This repository contains the materials for an academic assignment implementing a **Retrieval-Augmented Generation (RAG)** system.  
The goal is to generate accurate, verified, and contextually grounded answers **strictly based on the digitized content of the Constitution of the Islamic Republic of Pakistan (1973)**.

The architecture is designed to overcome typical LLM limitations—such as hallucination, outdated knowledge, or lack of verifiability—by constraining the model's output to retrieved constitutional text.

---

## 🚀 System Architecture and Technology Stack

The application uses a modular, multi-component architecture built on **LangChain** for pipeline orchestration and **Ollama** for running local models.

### 🔧 Key Components

| Component       | Technology / Model          | Role |
|----------------|-----------------------------|------|
| **Frontend**   | Streamlit                   | User interface for query input and response display. |
| **Vector Store** | Chroma DB                 | Stores embeddings of constitutional text for semantic search. |
| **Embedding Model** | `nomic-embed-text` (Ollama) | Converts text into vector embeddings for retrieval. |
| **LLM Engine** | `deepseek-r1:1.5b` (Ollama) | Generates grounded answers using retrieved context. |

---

## 🔁 RAG Pipeline Overview

1. **Query Input**  
   The user types a natural-language question into the Streamlit application.

2. **Vectorization**  
   The query is embedded using the `nomic-embed-text` embedding model.

3. **Retrieval**  
   A similarity search (`k=1`) is performed against Chroma DB to fetch the *single most relevant* chunk of constitutional text.

4. **Augmentation**  
   The retrieved chunk is combined with the user query to form an augmented prompt.

5. **Inference**  
   The prompt is passed to the `deepseek-r1:1.5b` model running in deterministic mode (`temperature=0.2`) to ensure maximum faithfulness.

6. **Response Display**  
   The grounded, concise answer is returned to the user.

---

## ✨ Implementation Highlights

### ✔ Real-Time Context Grounding  
Each query triggers an immediate retrieval step, ensuring that the LLM answers *only using the constitutional text*, minimizing hallucinations.

### ⚡ Performance Optimization  
Using `k=1` drastically reduces the token load while preserving relevance—leading to faster, lower-latency responses.

### 🧩 Modular Architecture  
Built with LangChain modules from `langchain-ollama` and `langchain-community`, allowing easy upgrades or component swapping (LLM, embeddings, vector store).

---

## 🛠️ Setup and Installation

### 📌 Prerequisites

- **Python 3.9+**
- **Ollama Runtime**
- Required models pulled locally:

```bash
ollama pull deepseek-r1:1.5b
ollama pull nomic-embed-text


📦 **Installation**

# 1. Clone the repository
```bash
git clone <https://github.com/nida-akhtar/ConstitutionOfPakistanRAG.git>
cd <ConstitutionOfPakistanRAG>


###2. Install Python dependencies
pip install -r requirements.txt

The requirements file typically includes:

streamlit

langchain

langchain-ollama

langchain-community

chromadb

-----








# 🇵🇰 Constitutional Q&A System — Retrieval-Augmented Generation (RAG)

This repository implements a **Retrieval-Augmented Generation (RAG)** system designed to answer questions **strictly based on the Constitution of the Islamic Republic of Pakistan (1973)**.

Using **LangChain**, **Chroma**, and **Ollama**, the system retrieves relevant constitutional text and generates grounded, verifiable answers with minimal hallucination.

---

## 🚀 System Overview

The application works by retrieving the most relevant textual chunks from the constitution and feeding them into an LLM to ensure responses are always:

- Accurate  
- Contextually grounded  
- Traceable to source text  

---

## 🧱 Tech Stack

| Component | Technology / Model | Purpose |
|----------|--------------------|----------|
| **Frontend** | Streamlit | User interface |
| **Vector Store** | ChromaDB | Stores embeddings and performs semantic search |
| **Embedding Model** | `nomic-embed-text` (Ollama) | Converts constitutional text into vector embeddings |
| **LLM** | `deepseek-r1:1.5b` (Ollama) | Generates grounded answers using retrieved context |

---

## 🔁 RAG Pipeline

### **1. User Query**  
The user enters a question through the Streamlit UI.

### **2. Embedding**  
The query is embedded via:  
```python
OllamaEmbeddings(model="nomic-embed-text")

### 3. Retrieval  
Chroma performs a semantic search (**k=3**) on constitutional text.

### 4. Prompt Augmentation  
Retrieved chunks are inserted into a structured prompt.

### 5. LLM Inference  
The **deepseek-r1:1.5b** model generates a grounded answer (`temperature=0.2`).

### 6. Display  
The answer is shown in the UI.

---

## ✨ Features

### ✔ Reliable Answering (No Hallucinations)
- Answers rely **only** on retrieved constitutional text.  
- If context is insufficient, the system clearly states so.

### ✔ Fully Local
Runs entirely on **Ollama**, ensuring privacy and offline capability.

### ✔ Modular & Extensible
Uses LangChain modules from:  
- `langchain-ollama`  
- `langchain-community`  

Easily swap LLMs, embeddings, or vector stores.

---

## 🛠️ Setup & Installation

### 📌 Prerequisites

- **Python 3.9+**  
- **Ollama installed locally**

Pull required models:

```bash
ollama pull deepseek-r1:1.5b
ollama pull nomic-embed-text

# 📦 Installation

## 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo>

###2️⃣ Install Python dependencies
```bash
pip install -r requirements.txt


#Typical dependencies:

-streamlit

-langchain

-langchain-ollama

-langchain-community

-langchain-text-splitters

-chromadb

-pypdf

###🧰 Building the Vector Database

Run the following script to process the PDF and build the Chroma vector store:
```bash
python rag_constitution.py


This generates a persistent vector database in:
```bash
constitution_db/

###▶️ Running the Streamlit App
```bash
streamlit run app1.py

###3📁 Project Structure
├── app1.py
├── rag_constitution.py
├── requirements.txt
├── Constitution_of_Pakistan.pdf
└── constitution_db/         # Generated after embedding
###📝 Notes
All responses are derived only from retrieved constitutional text.

If insufficient context exists, the model communicates this clearly.

For best accuracy, ensure the PDF is clean and properly OCR-processed.

###📜 License
This project is intended for academic and educational use.
You may modify and extend it freely.