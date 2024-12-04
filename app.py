import streamlit as st
from rag import Agent

agent = Agent()

def chat(message):
    # Create a single string from the history, concatenating each message
    conversation = "\n".join([f"{message['role']}: {message['content']}" for message in message])
    #print(f"Conversation: {conversation}")
    response = agent.chatAgent(conversation)
    return response

def show_citation(citations):
    unique_citations = {}
        
    # Collect unique citations by URL and page
    for c in citations:
        source = c.metadata['source']
        page = c.metadata['page']
        
        # Generate a citation link format
        citation_key = f"{source} (Page {page})"
        citation_value = f"Source: {source}, Page: {page}"

        if citation_key not in unique_citations:
            unique_citations[citation_key] = citation_value
        
    # Display citations with clickable titles and page numbers
    with st.expander("Reference"):
        for citation_key, citation_value in unique_citations.items():
            # Make the source clickable if it's a URL or file path
            st.markdown(citation_value)

# Set the title of the app
st.title("Nigeria Knowledge Bot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Display chat history (with citations for previous responses)
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and message.get("citations"):
            show_citation(message["citations"])

# Input field for the user to type a question
user_input = st.chat_input("Let's chat about Nigeria...")


# Display the chatbot's response
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Prepare history without citations (only user and assistant content)
    history = [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history]
    #print(f"Session: {history}")

    try:
        response = chat(history)
        citations = response['context']

        # Add the bot's response and citations to the chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response['answer'], "citations": citations})

        with st.chat_message("assistant"):
            st.markdown(response['answer'])
            if citations:
                show_citation(citations)
    except Exception as e:
        print(f"Error: {e}")