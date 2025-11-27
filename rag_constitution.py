from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

PDF_PATH = "Constitution_of_Pakistan.pdf"

# Step 1: Load PDF
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()

# Step 2: Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)
chunks = splitter.split_documents(docs)

# Step 3: Create embeddings using Ollama
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Step 4: Create vector DB
db = Chroma.from_documents(chunks, embedding=embeddings, persist_directory="constitution_db")

print("Database built!")
