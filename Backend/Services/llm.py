from openai import OpenAI
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

#openrouter setup
openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def ask_openrouter(prompt):

    response = openrouter_client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "system",
                "content": "You are Aura, a helpful personal AI assistant. Keep responses concise and conversational."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

#gemini setup
models = [
    "gemini-3.6-flash",
    "gemini-3.8-flash",
    "gemini-3.7-flash",
    "gemini-3.5-flash",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite"
]

gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"),
                      http_options=types.HttpOptions(timeout=10000))

def ask_gemini(prompt):

    for model in models:

        try:
            print(f"Trying: {model}")

            response = gemini_client.models.generate_content(
                model=model,
                contents=prompt
            )

            print(f"Success: {model}")
            return response.text

        except Exception as e:
            print(f"{model} failed: {e}")
            continue

    return None


def ask_llm(prompt):

    # -------------------------
    # 1. Try Gemini
    # -------------------------

    response = ask_gemini(prompt)

    if response:
        return response


    # -------------------------
    # 2. Gemini failed
    # Try OpenRouter
    # -------------------------

    print("Gemini unavailable. Switching to OpenRouter...")

    response = ask_openrouter(prompt)

    if response:
        return response


    # -------------------------
    # 3. Both failed
    # -------------------------

    return "Sorry, all AI providers are currently unavailable."

print(ask_llm('hey!'))