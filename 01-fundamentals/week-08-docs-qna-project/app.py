import streamlit as st

# Week 08 · Docs Q&A (Pro Mode)
st.title("Docs Q&A — Week 08")

q = st.text_input("Ask a question")
show_ctx = st.checkbox("🔍 Show retrieved context", value=False)

# TODO: load retriever, generator, cache

if q:
    # TODO: implement pipeline (retrieve -> generate -> log metrics -> cache)
    st.markdown("**Answer will appear here...**")

    if show_ctx:
        with st.expander("Retrieved passages"):
            st.write("TODO: show retrieved chunks + metadata")
