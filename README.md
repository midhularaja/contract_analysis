A lightweight GenAI-powered legal assistant for Indian SMEs that analyzes contracts and highlights legal risks in plain business language.
Supports PDF, DOCX, and TXT contracts in English and Hindi, provides clause-level risk insights, simplified explanations, and actionable advice.
Built using Python, FastAPI, and Streamlit, with local processing to maintain confidentiality and audit logs for legal review.

How to Run the Project

Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

Install dependencies using requirements file
pip install -r requirements.txt

Start backend server (FastAPI)
python main.py

Backend will run at
http://127.0.0.1:8000

Start frontend application (Streamlit)
streamlit run app.py

Application will open in browser at
http://localhost:8501

Upload contract file
Supported formats: PDF, DOCX, TXT
View contract type, risk score, clause explanations, and actionable advice

Note
Backend must be running before starting the Streamlit app.
All contract processing happens locally to maintain confidentiality.
