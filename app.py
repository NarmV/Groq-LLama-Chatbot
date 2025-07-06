import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
 
# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ")
 
# Verify API key
if not api_key:
    st.error("GROQ_API_KEY is missing. Please set it in your .env file.")
    st.stop()
 
# Streamlit page setup
st.set_page_config(page_title="Groq Chatbot", layout="centered")
st.title("🤖 Chat with Groq (LLaMA 3)")
 
# Set up Groq LLM via LangChain
llm = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",  # You can use llama3-70b-8192 or mixtral-8x7b-32768
    groq_api_key=api_key,
    temperature=0.7
)
 
# Initialize memory and conversation chain
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()
    st.session_state.chain = ConversationChain(
        llm=llm,
        memory=st.session_state.memory,
        verbose=False
    )
 
# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
 
# Display previous messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
 
# Chat input
user_input = st.chat_input("Type your message here...")
 
if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
 
    # Get LLM response
    response = st.session_state.chain.run(user_input)
 
    # Display assistant response
    st.chat_message("assistant").markdown(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})
 
 