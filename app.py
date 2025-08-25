# app.py
import os
from pathlib import Path
import streamlit as st

# ---------- Page / Theme ----------
st.set_page_config(
    page_title="CAI | Chief AI Officer",
    layout="wide",
    page_icon="🧠",
)

# ---------- Branding CSS ----------
st.markdown(
    """
    <style>
        .stApp { background-color: #0c0c0c; color: white; }
        .sidebar .sidebar-content { background-color: #1a1a1a; color: white; }
        .block-container { padding-top: 2rem; }
        .css-1d391kg { background-color: #1a1a1a; } /* text input */
        .stChatMessage.user {
            text-align: right; background-color: #1a1a2a;
            border-radius: 18px; padding: 0.5rem 1rem; margin: 0.25rem 0; color: white;
        }
        .stChatMessage.assistant {
            background-color: #2c2c2c; border-radius: 18px;
            padding: 0.5rem 1rem; margin: 0.25rem 0; color: white;
        }
        .stButton>button { background-color: #e63946; color: white; }
        .stMarkdown a { color: #e63946; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Header / Logo ----------
logo_path = Path("ChatGPT Image May 31, 2025, 02_22_21 PM.png")
if logo_path.exists():
    st.image(str(logo_path), width=100)
st.title("CAI – Chief AI Officer")

# ---------- Session State ----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------- Lazy, Cached Heavy Init ----------
@st.cache_resource(show_spinner="Loading knowledge base…")
def get_query_engine():
    """
    Do ALL heavy imports and work inside this function so nothing runs at import time.
    This is called once per container; subsequent calls reuse the cached resource.
    """
    # Heavy imports inside (avoid top-level overhead)
    from dotenv import load_dotenv
    load_dotenv()  # loads OPENAI_API_KEY, LLAMA_CLOUD_API_KEY, etc.

    # Anything from LlamaIndex should be imported here
    from load_documents import load_index_from_docs  # your helper
    # If your loader uses llama_parse or other heavy libs, they will load here too.

    index = load_index_from_docs()               # heavy: parse/build/load index
    return index.as_query_engine()               # keep only the query engine cached

# ---------- Sidebar ----------
with st.sidebar:
    st.header("📂 Document Tools")
    st.markdown("All documents are loaded from the `/docs` folder.")
    warm = st.button("⚡ Warm up knowledge base")
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []

# Manual warm-up (optional but useful so user can trigger it)
if warm:
    _ = get_query_engine()
    st.success("Knowledge base is ready.")

# ---------- Chat UI ----------
user_input = st.chat_input("Ask CAI a question or paste an email to get help drafting a reply:")

if user_input:
    # Ensure the query engine is ready (first call shows spinner once)
    query_engine = get_query_engine()

    st.session_state.chat_history.append(("user", user_input))
    try:
        response = query_engine.query(user_input)
        st.session_state.chat_history.append(("assistant", str(response)))
    except Exception as e:
        st.session_state.chat_history.append(
            ("assistant", f"Oops — I hit an error while querying: `{e}`")
        )

# ---------- Render history ----------
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)
