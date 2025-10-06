# Azure AI Chatbot

A simple Python chatbot that uses Azure OpenAI (GPT-4o) to generate responses.

## Features

- Command-line interface
- Connects to Azure OpenAI service
- Loads credentials from `.env` file

## Setup

1. Clone the repository.
2. Add your Azure OpenAI credentials to the `.env` file:
   - `AZURE_OPENAI_API_KEY`
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_MODEL_NAME`
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the chatbot:
   ```
   python chatbot.py
   ```

## Architecture

See `architecture.md` for design details and diagrams.
