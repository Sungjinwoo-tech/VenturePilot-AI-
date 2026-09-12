import os
import streamlit as st
from rag_engine import RAGEngine

st.set_page_config(page_title="VenturePilot AI", page_icon="ðŸš€", layout="wide")

st.markdown("""
<style>
.block-container {max-width: 1200px; padding-top: 2rem;}
.hero {padding: 1.4rem 1.6rem; border-radius: 18px; background: linear-gradient(135deg,#0b1220,#16243d); color:white; margin-bottom:1rem;}
.hero h1 {margin:0; font-size:2.5rem;}
.hero p {margin:.45rem 0 0; color:#d7e2f0;}
.source-card {padding:.8rem 1rem; border:1px solid #d9dee8; border-radius:12px; margin:.35rem 0;}
.small {font-size:.86rem; color:#667085;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>VenturePilot AI</h1>
<p>Pakistan Cyber Law RAG Assistant â€” ask questions and get answers grounded in the loaded legal documents.</p>
</div>
""", unsafe_allow_html=True)

@st.cache_resource(show_spinner=False)
def load_engine():
    return RAGEngine()

try:
    with st.spinner("Preparing the legal knowledge base and embeddings..."):
        engine = load_engine()
except Exception as exc:
    st.error("VenturePilot AI could not initialize the knowledge base.")
    st.exception(exc)
    st.stop()

with st.sidebar:
    st.header("VenturePilot AI")
    st.caption("Agent-ready RAG application")
    st.divider()
    st.subheader("Knowledge base")
    for item in engine.source_status:
        st.write(("âœ… " if item["ok"] else "âš ï¸ ") + item["name"])
    st.divider()
    st.subheader("Settings")
    top_k = st.slider("Retrieved passages", 2, 8, 5)
    temperature = st.slider("Answer creativity", 0.0, 0.7, 0.2, 0.1)
    st.caption("For legal questions, treat the response as informationalâ€”not legal advice.")

st.subheader("Ask about Pakistan cyber law")
question = st.text_area(
    "Your question",
    placeholder="Example: What does PECA say about unauthorized access to an information system?",
    height=120,
)

col1, col2 = st.columns([1, 5])
with col1:
    ask = st.button("Ask VenturePilot", type="primary", use_container_width=True)
with col2:
    st.markdown('<span class="small">Answers are generated from retrieved passages from the knowledge base.</span>', unsafe_allow_html=True)

if ask:
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Retrieving relevant law and generating an answer..."):
            result = engine.answer(question.strip(), top_k=top_k, temperature=temperature)
        st.markdown("### Answer")
        st.write(result["answer"])

        if result.get("sources"):
            st.markdown("### Retrieved sources")
            for i, src in enumerate(result["sources"], 1):
                st.markdown(
                    f'<div class="source-card"><b>{i}. {src["source"]}</b> â€” page {src.get("page", "N/A")}<br>{src["preview"]}</div>',
                    unsafe_allow_html=True,
                )

st.divider()
st.caption("VenturePilot AI â€¢ RAG prototype for the Pak Angels Gen-Agentic AI hackathon â€¢ Verify important legal matters with a qualified lawyer and the latest official Gazette/law source.")
