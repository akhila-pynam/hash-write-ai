import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Get API key safely
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def correct_grammar(text):
    if len(text.split()) < 30:
        return "Please enter at least 30 words."

    try:
        response = model.generate_content(
            f"Correct grammar and improve clarity:\n{text}"
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


def generate_paragraph(topic):
    try:
        response = model.generate_content(
            f"Write a human-like paragraph about {topic}"
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"