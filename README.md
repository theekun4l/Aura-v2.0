# 🤖 Aura V1.5

Aura is a Python-based personal AI assistant that evolved from a terminal-based assistant into an interactive Streamlit web application.

Aura V1.5 introduces a modern chat interface, LLM integration, animated responses, and command-based actions.

---

## ✨ Features

- 💬 Interactive Streamlit chat interface
- 🧠 LLM-powered responses using OpenRouter
- ⚡ Command-based assistant actions
- 🎵 Play music through YouTube
- ▶️ Open YouTube
- 📸 Open Instagram
- 🕐 Date and time responses
- 😂 Joke responses
- 💭 Animated "Aura is thinking" indicator
- 💾 Chat history using Streamlit session state
- 🔐 API keys managed through environment variables

---

## 🛠️ Tech Stack

- Python
- Streamlit
- OpenRouter
- OpenAI Python SDK
- python-dotenv
- PyWhatKit
- PyJokes
- Requests

---

## 📁 Project Structure

```text
Aura/
│
├── features/
│   ├── actions.py
│   ├── api.py
│   ├── replies.py
│   └── utils.py
│
├── LLM/
│   └── llm.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore