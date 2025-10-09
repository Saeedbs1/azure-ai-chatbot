# Azure AI Chatbot Architecture Documentation

## Overview

This document explains the architecture and design decisions for the Azure AI Chatbot project.

## Architecture Diagram

- The initial diagram (`azure-ai-chatbot.drawio.svg`) shows the following components:
  - **User**: Interacts with the chatbot via a command-line interface.
  - **Application**: Python app running locally, handling user input and responses.
  - **Azure OpenAI Resource**: Cloud service providing AI-powered responses (GPT-4o model).
  - **Resource Group**: Azure container for managing resources (e.g., `rg-internship`).

## Data Flow

1. **User** enters a message in the chatbot interface.
2. **Application** receives the message and sends it to the Azure OpenAI resource using the `AzureOpenAI` from `openAI` Library.
3. **Azure OpenAI** processes the request using the specified model (e.g., GPT-4o) and returns a response.
4. **Application** displays the response to the user.

## Component Interactions

- The application authenticates with Azure OpenAI using credentials from the `.env` file.
- All requests and responses flow through the application, which acts as a bridge between the user and Azure OpenAI.
- The Resource Group organizes and manages the Azure OpenAI resource and any future Azure services.
