from datetime import datetime
from .llm import ask_llm
from .api import GetData


class Aura(GetData):

    def date_time(self):
        date_today = datetime.now().strftime("%d-%m-%y")
        time_now = datetime.now().strftime("%I:%M %p")

        return {
            "type": "response",
            "message": f"Today is {date_today}. Current time is {time_now}."
        }

    def command(self, user_input):

        user_input = user_input.lower().strip()

        if "youtube" in user_input:
            return {
                "type": "open_url",
                "url": "https://youtube.com"
            }

        elif "instagram" in user_input:
            return {
                "type": "open_url",
                "url": "https://instagram.com"
            }

        elif "date" in user_input or "time" in user_input:
            return self.date_time()

        elif 'weather' in user_input:
            response = ask_llm(f"""
Extract the city name from this user request.

User request: {user_input}

Return ONLY the city name.
"""
)

            weather = self.weather(response)

            if not weather:
                return {
                    "type": "error",
                    "message": "Weather information nahi mil paayi."
                }

            temp, condition, city = weather

            return {
                "type": "response",
                "message": f"The temperature in {city} is {temp:.0f}°C with {condition}."
            }
        elif 'github' in user_input:
            response = ask_llm(
    f"""
Extract the GitHub username from this user request.

User request: {user_input}

Return ONLY the GitHub username.
Do not explain anything.
Do not add extra text.

Examples:
"Give me GitHub info of torvalds" → torvalds
"Show me the GitHub profile of theekun4l" → theekun4l
"Tell me about github user octocat" → octocat
"""
)

            
            print("GITHUB USERNAME:", response)

            github = self.git_hub_info(response.strip())

            print("GITHUB RESPONSE:", github)

            if not github:
                return {
            "type": "error",
            "message": "GitHub user nahi mila."
        }

            login, name, bio, location, repos, followers, following, url = github

            return {
        "type": "response",
        "message": (
            f"GitHub user {login} has {repos} public repositories, "
            f"{followers} followers and {following} following."
        ),
        "profile": url
    }

        elif 'fact' in user_input:
            response = self.facts()

            return {
                            "type": "response",
                            "message": response
                        }
        elif 'joke' in user_input:
            response = self.get_joke()

            return {
                            "type": "response",
                            "message": response
                        }
       
        elif 'location' in user_input:
            response = self.get_location()
            return {
                            "type": "response",
                            "message": response
            }
        
        elif 'price' in user_input:
            currency = crypto_list = [
    "bitcoin",
    "ethereum",
    "solana",
    "dogecoin",
    "cardano",
    "ripple",
    "binancecoin",
    "polkadot",
    "avalanche-2",
    "shiba-inu",
    "litecoin",
    "tron",
    "chainlink",
    "matic-network",
    "uniswap"
]   
            for c in currency:
                if c in user_input:
                    return {
                "type": "response",
                "message": f"Price of {c} is ₹{self.crypto_price(c)}"
            }
        else:
            response = ask_llm(user_input)

            return {
                "type": "response",
                "message": response
            }