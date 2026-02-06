import streamlit as st
from processor import process_contract_logic

st.set_page_config(page_title="SME Legal Analyzer", layout="centered")

st.title("📄 SME Legal Contract Analyzer")

uploaded_file = st.file_uploader(
    "Upload contract file (PDF / DOCX / TXT)",
    type=["pdf", "docx", "doc", "txt"]
)

if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    filename = uploaded_file.name

    with st.spinner("Analyzing contract..."):
        result = process_contract_logic(file_bytes, filename)

    st.success("Analysis completed ✅")

    st.subheader("📌 Contract Summary")
    st.json(result)
