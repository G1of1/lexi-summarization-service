# LexiAI – Summarization Service

The Summarization Service is a microservice responsible for generating structured summaries from user-provided text using the Gemini API.

It supports multiple summarization levels and returns responses strictly in JSON format.

---

## 🚀 Features

- Text summarization via LLM
- Adjustable summary levels (short, medium, detailed)
- JSON-only structured responses
- Dockerized deployment
- CI/CD pipeline with GitHub Actions

---

## 🏗 Architecture

This service:
- Receives text from the API Gateway
- Formats prompts for the LLM
- Sends request to Gemini
- Returns structured JSON response

---

## 📦 Tech Stack

- Python
- FastAPI
- LLM Provider (Gemini)
- Docker(Deployment)
- Render(Deployment)

---
