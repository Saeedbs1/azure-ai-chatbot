import os
from dotenv import load_dotenv
load_dotenv()
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
  api_key= os.getenv("AZURE_OPENAI_API_KEY"),
  api_version="2024-05-01-preview"
)


def chat():
    print("Welcome to Azure AI Chatbot")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        try:
            resp = client.chat.completions.create(
                model=os.getenv("AZURE_OPENAI_MODEL_NAME"),
                messages=[
                    {"role": "system", "content": "You are a helpful chatbot."},
                    {"role": "user", "content": user_input},
                ],
                temperature=0.4,  
            )
            print("Bot:", resp.choices[0].message.content)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat()
