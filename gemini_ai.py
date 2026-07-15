import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

# Read API Key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise Exception("❌ GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


# ----------------------------------------
# AI Summary + Risk Analysis
# ----------------------------------------
def generate_summary(document_text):

    prompt = f"""
You are an AI Legal Document Analyzer.

Analyze the following legal document.

Return ONLY in this format.

📄 Summary:
Write 4 to 5 lines.

⚠ Risk Level:
Low / Medium / High

📊 Risk Score:
Give score out of 100.

📑 Important Clauses:
- Clause 1
- Clause 2
- Clause 3
- Clause 4

💡 Recommendation:
Give one short recommendation.

Legal Document:

{document_text}
"""

    response = model.generate_content(prompt)

    return response.text


# ----------------------------------------
# Ask AI
# ----------------------------------------
def ask_question(document_text, question):

    prompt = f"""
You are an AI Legal Assistant.

Legal Document:

{document_text}

User Question:

{question}

Answer in simple English.
Maximum 5 lines.
"""

    response = model.generate_content(prompt)

    return response.text