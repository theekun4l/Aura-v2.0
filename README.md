# ✨ Aura V2.0

Aura is a personal AI assistant built with **JavaScript, FastAPI, Gemini, and OpenRouter**.

Aura V2.0 is a complete web-based version of the assistant with a responsive UI, AI chat, voice interaction, API integrations, and browser-based commands.

## 🚀 Live Demo

**Frontend:**  
https://aura-v2-frontend.onrender.com

**Backend API:**  
https://aura-v2-backend.onrender.com

---

## ✨ Features

- 💬 AI-powered chat
- 🤖 Gemini + OpenRouter integration
- 🔄 LLM provider fallback
- 🎤 Voice input using Web Speech API
- 🔊 Voice output using SpeechSynthesis API
- 🌐 Browser-based commands
- 📰 News API integration
- 🌦️ Weather API integration
- 💱 Currency exchange API integration
- 🌓 Light/Dark theme
- 📱 Responsive mobile-friendly UI
- ⏳ Loading animation while Aura processes requests
- 💬 Dynamic chat history during the current session
- 🔐 Environment-based API key management

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Web Speech API
- Font Awesome

### Backend
- Python
- FastAPI
- Pydantic
- Uvicorn
- Requests

### AI
- Google Gemini
- OpenRouter

### APIs
- News API
- Weather API
- Exchange Rate API

### Deployment
- Render

---

## 🏗️ Architecture

```text
                 ┌──────────────────────┐
                 │     User / Phone     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    HTML/CSS/JS       │
                 │     Frontend         │
                 └──────────┬───────────┘
                            │
                       HTTP Request
                            │
                            ▼
                 ┌──────────────────────┐
                 │       FastAPI        │
                 │       Backend        │
                 └──────────┬───────────┘
                            │
                ┌───────────┼───────────┐
                ▼           ▼           ▼
             Gemini     OpenRouter     APIs
                │           │         Weather
                │           │         News
                │           │         Currency
                └───────────┴───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Aura Response     │
                 └──────────────────────┘
```

---

## 📁 Project Structure

```text
Aura-v2.0/
│
├── Backend/
│   ├── Features/
│   │   └── replies.py
│   │
│   ├── Services/
│   │   ├── api.py
│   │   ├── aura.py
│   │   └── llm.py
│   │
│   └── main.py
│
├── Frontend/
│   ├── assets/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🎤 Voice Interaction

Aura V2.0 uses the browser's Web Speech API for voice interaction.

### Voice Input

```text
User speaks
    ↓
Speech Recognition
    ↓
Text
    ↓
FastAPI
    ↓
Aura
```

### Voice Output

```text
Aura Response
    ↓
SpeechSynthesis
    ↓
Spoken Response
```

---

## 🧠 AI Provider Fallback

Aura supports multiple AI providers.

```text
User Request
    ↓
Primary LLM
    ↓
Success ──────→ Response
    │
    └── Error / Limit
            ↓
       Fallback Provider
            ↓
         Response
```

This allows Aura to continue responding when one provider reaches its limit or encounters an error.

---

## 🌐 Browser Commands

Aura can handle browser-based commands such as opening websites.

For example:

```text
User: Open YouTube
        ↓
Aura detects command
        ↓
Frontend executes browser action
        ↓
YouTube opens
```

Browser actions are handled on the client side, allowing them to work when Aura is deployed online.

---

## 🔐 Environment Variables

API keys are stored as environment variables instead of being hard-coded.

```env
OPENROUTER_API_KEY=your_key
GEMINI_API_KEY=your_key
WEATHER_API_KEY=your_key
NEWS_API_KEY=your_key
EXCHANGE_RATE_API_KEY=your_key
```

**Never commit your `.env` file or API keys to GitHub.**

---

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/theekun4l/Aura-v2.0.git
cd Aura-v2.0
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_key
GEMINI_API_KEY=your_key
WEATHER_API_KEY=your_key
NEWS_API_KEY=your_key
EXCHANGE_RATE_API_KEY=your_key
```

### 5. Start the FastAPI backend

```bash
uvicorn Backend.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### 6. Open the frontend

Open the `Frontend/index.html` file using a local development server such as VS Code Live Server.

---

## ☁️ Deployment

Aura V2.0 is deployed using **Render**.

```text
Frontend → Render Static Site
Backend  → Render Web Service
```

The frontend communicates with the deployed FastAPI backend through HTTP requests.

---

## 📚 What I Learned

While building Aura V2.0, I practiced:

- JavaScript DOM manipulation
- Event handling
- Async/Await
- Fetch API
- REST API integration
- JSON requests/responses
- POST requests
- CORS
- FastAPI
- Pydantic
- Environment variables
- API integration
- LLM integration
- Voice Recognition
- Speech Synthesis
- Responsive web design
- Frontend/backend architecture
- Deployment with Render

---

## 🔮 Future Improvements

Possible future improvements:

- Persistent conversation history
- Long-term AI memory
- Database integration
- More advanced tool calling
- More automation commands
- Authentication
- File uploads
- RAG
- More AI capabilities

---

## 👨‍💻 Author

**Kunal Maheshwari**

GitHub:
[https://github.com/theekun4l](https://github.com/theekun4l)

---

⭐ Aura V2.0 is a personal project built while learning **Web Development, APIs, FastAPI, and Generative AI**.