import streamlit as st
import requests
import json

st.set_page_config(page_title="SME Legal AI", layout="wide")

st.markdown("""
    <style>
    [data-testid="stMetricValue"] { color: #1f77b4 !important; font-size: 2rem !important; }
    [data-testid="stMetricLabel"] { color: #31333F !important; font-weight: bold !important; }
    [data-testid="stMetric"] { background-color: #ffffff !important; border: 1px solid #dee2e6; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚖️ SME Legal Assistant")
uploaded_file = st.file_uploader("Upload Contract", type=['pdf', 'docx', 'txt'])

if uploaded_file:
    with st.spinner("Analyzing..."):
        try:
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
            response = requests.post("http://127.0.0.1:8000/analyze", files=files)
            data = response.json()
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Contract Type", data.get('contract_type'))
            col2.metric("Risk Score", f"{data.get('risk_score')}/10")
            col3.metric("Jurisdiction", data.get('entities', {}).get('jurisdiction'))

            st.subheader("Detailed Breakdown")
            for clause in data.get('clauses', []):
                with st.expander(f"📌 {clause.get('title')} - {clause.get('risk_level')} Risk"):
                    st.write(f"**Meaning:** {clause.get('plain_language_explanation')}")
                    st.warning(f"**Advice:** {clause.get('actionable_insight')}")
        except:
            st.error("Backend Error. Makesure main.py is running.")