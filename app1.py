import streamlit as st
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.vectorstores import Chroma

st.set_page_config(page_title="Constitution Q&A", page_icon="📜")
st.markdown("<h1 style='text-align:center; color:purple;'>Ask about Pakistan's Constitution</h1>", unsafe_allow_html=True)

db = Chroma(
    persist_directory="constitution_db",
    embedding_function=OllamaEmbeddings(model="nomic-embed-text")
)

llm = OllamaLLM(
    model="deepseek-r1:1.5b",
    temperature=0.2,
    streaming=False
)

query = st.text_input("Enter your question:")

if query:
    with st.spinner("Retrieving answer..."):
        docs = db.similarity_search(query, k=3)
        context = "\n\n".join([d.page_content for d in docs])

        prompt = f"""
Use the following context to answer the question.
If the context does not contain enough information, say so.

Context:
{context}

Question: {query}

Answer:
"""

        resp = llm.generate([prompt])
        answer = resp.generations[0][0].text

    st.markdown(f"**Answer:** {answer}")
