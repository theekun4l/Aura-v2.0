import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

#


# response = requests.get(base_url)
# data =  response.json()
# print(data)
# data = response.json()
# joke = data["value"]
# print(joke)


class GetData:
    def get_response(self,base_url):
        response = requests.get(base_url)
        return response.json()
    def get_joke(self):
        base_url = "https://api.chucknorris.io/jokes/random"
        data = self.get_response(base_url)
        return data['value']

    def facts(self):
        base_url = "https://uselessfacts.jsph.pl/random.json?language=en"
        data = self.get_response(base_url)
        return data['text']

    def git_hub_info(self):
            username = input("Enter GitHub username: ")
            url ="https://api.github.com/users/" + username
            data = self.get_response(url)
            if data['message']:
                return False
            else:
                return data['login'],data['name'],data['bio'],data['location'],data['public_repos'],data['followers'],data['following'],data['html_url']

    def crypto_price(self):
        crypto_currency  = input("Enter coin name: ").lower()
        base_url = "https://api.coingecko.com/api/v3/simple/price?ids=" + crypto_currency + "&vs_currencies=inr"
        data = self.get_response(base_url)
        if crypto_currency not in data:
            return False
        return data[crypto_currency]['inr']

    def weather(self):
        city_name = input("Enter city name: ").strip().lower()
        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
        data = self.get_response(base_url)
        if data['cod'] != 200:
            return False
        return data['main']['temp'],data['weather'][0]['description'],data['name']

    def get_location(self):
        base_url = "http://ip-api.com/json/"
        data = self.get_response(base_url)
        return f"City: {data['city']},country: {data['country']},ISP: {data['isp']}"

    def get_meaning(self):
        word = input("Enter Word : ").strip().lower()
        base_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        data = self.get_response(base_url)
        if isinstance(data, dict):
            return "Nahi mila..."
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        return f"{word}: {definition}"








