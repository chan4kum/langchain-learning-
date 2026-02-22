import os

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("VERTEX_API_KEY")

url = f"https://aiplatform.googleapis.com/v1/publishers/google/models/gemini-2.5-flash-lite:streamGenerateContent?key={API_KEY}"

payload = {
    "contents": [
        {"role": "user", "parts": [{"text": "Explain how AI works in a few words"}]}
    ]
}

response = requests.post(url, json=payload)
data = response.json()

# Concatenate all text parts from candidates
output_text = ""
for item in data:
    for candidate in item.get("candidates", []):
        for part in candidate["content"]["parts"]:
            output_text += part.get("text", "")

print("Model Response:", output_text.strip())
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
response = llm.invoke("Explain LangChain in one sentence.")
print(response.content)
