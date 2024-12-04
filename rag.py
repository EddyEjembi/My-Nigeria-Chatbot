import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_xai import ChatXAI
from prompt import prompt

load_dotenv()

XAI_API_KEY = os.getenv("XAI_API_KEY")

class Agent:
    def __init__(self,):
        # Load the embedding model
        self.embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        # Load Chat Model
        self.llm = ChatXAI(
            xai_api_key=XAI_API_KEY,
            model="grok-beta",
        )

        # Load the vectorstore
        self.vectorstore = FAISS.load_local("VECTOR-DB", self.embedding_model, allow_dangerous_deserialization=True)

        self.retriever = self.vectorstore.as_retriever()

        # System Prompt
        self.System_prompt = prompt()

    def chatAgent(self, query):
        system_prompt = (
            f"{self.System_prompt}"
            "\n\n"
            "{context}"
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )


        question_answer_chain = create_stuff_documents_chain(self.llm, prompt)
        rag_chain = create_retrieval_chain(self.retriever, question_answer_chain)

        results = rag_chain.invoke({"input": query})
        #print(f"Chatbot: {results}")

        return results
