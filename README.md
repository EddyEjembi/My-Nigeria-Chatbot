# *My Naija Chatbot*

A fun, interactive, and educative chatbot that answers questions about Nigeria.

Nigeria, officially the Federal Republic of Nigeria, is a country in West Africa. It is situated between the Sahel to the north and the Gulf of Guinea to the south in the Atlantic Ocean. It covers an area of 923,769 square kilometres (356,669 sq mi). With a population of more than 230 million (*Wikipedia*)

## About the Nigeria Chatbot
*My Naija Knowledge Bot* is an interactive tool designed to educate users about Nigeria, its people, and its rich history. It serves as an AI-based information assistant, offering insights into various aspects of the nation, such as its constitution, laws, culture, and historical milestones. The chatbot is powered by a Retrieval-Augmented Generation (RAG) agent that leverages curated documents to provide accurate, factual, and detailed responses, and Grok an [XAI](https://www.x.ai/) Large Language Model.


## How it Works
*My Naija Knowledge Bot* is a RAG agent that employs an LLM to provide factual and insightful answers to users questions. The Chatbot takes the personality of a fun, informative, educative and patriotic Nigerian with the aim of educating the public about the laws, acts, history, and rights of Nigerians. The chatbot tries to drive patriotism by personalizing it's response and encouraging users on their basic civic duties and rights.

### Knowledge Base
The data used as a source of reference and external source of information for the chatbot was gathered and curated from across the internet. Basic information, laws, acts, and history of Nigeria was gathered. One interesting fact about this chatbot, it references it's sources (including a link to the source and page number 🙂). You can access the data at this [repository](https://www.github.com/EddyEjembi/My-Nigeria-Chatbot/tree/main/My%20Nigeria). More data will be added soon 🤞.
The model ([Grok-beta](https://www.docs.x.ai/docs)) has it's own knowledge base which is still helpfull for the chatbot to generate response.

## Technical Details
The RAG pipeline was built using [Langchain](https://www.python.langchain.com/), and the sentence transformers from [HuggingFace](https://www.huggingface.co/) as the embedding model.

The Vector Database was built using [FAISS](https://www.github.com/facebookresearch/faiss) as it's a lightweight VectorDB that can run on cpu (considering the hosting environment).

The Chatbot is hosted on [Streamlit Cloud](https://www.streamlit.io/cloud) and can be accessed through this [url](https://my-naija-chat.streamlit.app/)


### Collaborate
Looking to learn more or collaborate, you can always reach me my [mail](mailto:eddyejembi2018@gmail.com).

Please do well to follow me on [X](https://www.x.com/eddyejembi) and let's connect on [LinkedIn](https://www.linkedin.com/in/eddyejembi/)