import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_ENDPOINT = "https://api.groq.ai/v1/llama3-70b-8192"  # Replace if endpoint differs

def ask_llm(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "max_output_tokens": 200  # roughly limits response length
    }
    response = requests.post(GROQ_ENDPOINT, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        # This depends on Groq response structure
        return data.get("completion", "")
    else:
        print("Groq API Error:", response.status_code, response.text)
        return "Sorry, I couldn't generate a response."
