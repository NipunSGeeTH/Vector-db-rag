import faiss
import numpy as np
import google.generativeai as genai
import pickle
import os
from dotenv import load_dotenv

# === CONFIG ===
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load saved FAISS index and paragraphs
index = faiss.read_index("bio_faiss.index")
with open("bio_paragraphs.pkl", "rb") as f:
    paragraphs = pickle.load(f)

# Simple Q&A function
def answer_question(question):
    # Just join all paragraphs as context
    context = " ".join(paragraphs)

    model = genai.GenerativeModel("gemini-2.5-flash")
    resp = model.generate_content(
        f"Answer the question based on all the text in Sinhala:\n{context}\nQuestion: {question}"
    )
    return resp.text.strip()


# Example
question = "ප්‍රභාසස්ලේශණය  විස්තර කරන්න ?"
answer = answer_question(question)
print("Answer:", answer)

# Ask another question without rebuilding database
# question2 = "ගෝලමානයෙන් මොකක්ද කරන්නේ?"
# answer2 = answer_question(question2)
# print("Answer:", answer2)
