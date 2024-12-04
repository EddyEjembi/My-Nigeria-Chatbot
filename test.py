from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS

# Load the embedding model
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Load the vectorstore
vectorstore = FAISS.load_local("VECTOR-DB", embedding_model, allow_dangerous_deserialization=True)

query = "What are some of the rights of Nigerian citizens?"
docs = vectorstore.similarity_search(query, k=5)  # Retrieve top 5 results

for doc in docs:
    print(f"Document: {doc.page_content}")
