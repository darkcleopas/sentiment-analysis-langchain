import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

print("Hello, I am a chatbot. Ask me anything!")