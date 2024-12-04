import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

#Load Document

# Path to the folder containing PDFs
folder_path = "./My Nigeria"
documents = []

# Load all PDFs
for file in os.listdir(folder_path):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(folder_path, file))
        documents.extend(loader.load())
        print(f"Loaded and extended document {file}")


#Split Document
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
print("Documents splitted")

#Initialize Embedding

# Load the embedding model
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Vectorize the text
embeddings = embedding_model.embed_documents([doc.page_content for doc in texts])

# Create and save a single VectorDB
vectorstore = FAISS.from_documents(texts, embedding_model)
vectorstore.save_local("VECTOR-DB")  # Persist directory
print("Vector DB saved successfully.")
