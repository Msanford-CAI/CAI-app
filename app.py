import streamlit as st
import openai
import os
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex, Document
from pathlib import Path
import pandas as pd
import docx2txt
import pdfplumber

from load_documents import load_index_from_docs

load_dotenv()

# App setup with CAI logo and new theme
st.set_page_config(
    page_title="CAI | Chief AI Officer",
    layout="wide",
    page_icon="🧠"
)

# Custom CSS for branding
st.markdown("""
    <style>
        .stApp {
            background-color: #0c0c0c;
            color: white;
        }
        .sidebar .sidebar-content {
            background-color: #1a1a1a;
            color: white;
        }
        .block-container {
            padding-top: 2rem;
        }
        .css-1d391kg {  /* Text input */
            background-color: #1a1a1a;
        }
        .stChatMessage.user {
            text-align: right;
            background-color: #1a1a2a;
            border-radius: 18px;
            padding: 0.5rem 1rem;
            margin: 0.25rem 0;
            color: white;
        }
        .stChatMessage.assistant {
            background-color: #2c2c2c;
            border-radius: 18px;
            padding: 0.5rem 1rem;
            margin: 0.25rem 0;
            color: white;
        }
        .stButton>button {
            background-color: #e63946;
            color: white;
        }
        .stMarkdown a {
            color: #e63946;
        }
    </style>
""", unsafe_allow_html=True)

# Display CAI logo
st.image("ChatGPT Image May 31, 2025, 02_22_21 PM.png", width=100)
st.title("CAI – Chief AI Officer")

openai.api_key = os.getenv("OPENAI_API_KEY")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Load the vector index
doc_index = load_index_from_docs()
query_engine = doc_index.as_query_engine()

# Sidebar
with st.sidebar:
    st.header("📂 Document Tools")
    st.markdown("All documents loaded from `/docs` folder.")
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []

# Chat interface
user_input = st.chat_input("Ask CAI a question or paste an email to get help drafting a reply:")
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    response = query_engine.query(user_input)
    st.session_state.chat_history.append(("assistant", str(response)))

# Display chat messages
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)