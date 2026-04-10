import webbrowser,time,random,pyjokes,os,pywhatkit
from features.utils import Text_Animator
from features.replies import Replies_class
from features.api import GetData
from datetime import datetime
class Aura(Text_Animator,Replies_class,GetData):
    def respond(self, text):
            self.type_animator(text, True)

    def open_insta(self,a):

        webbrowser.open("https://instagram.com")
        return   ["Aura: Opening Instagram..."]


    def open_youtube(self,a):
        webbrowser.open("https://youtube.com")
        return ["Aura: Opening YouTube..."]

    def open_chrome(self,a):
        os.system("start chrome")
        return ["Aura: Opening Chrome..."]

    def play_music(self,music):
            if 'music' in music:
                music = music.replace('music','').strip()
            pywhatkit.playonyt(music)
            return [f"Aura: Playing {music}..."]
    def date_time(self,a):
            date12 = datetime.now().strftime("%d-%m-%y")
            time_now = datetime.now().strftime("%I:%M %p")
            return [f"Aura: Today is {date12}. ",f"Aura: Current time is {time_now} "]
            # self.respond(f"Aura: Current time is {time_now} ")
    def joke(self,a):
        return [self.get_joke()]

    def get_fact(self,a):
        return [self.facts()]
    def github(self,user):
        if 'find' in user:
            user = user.replace('find','').strip()
        if 'on' in user:
            user = user.replace('on','').strip()
        result = self.git_hub_info(user)
        if result:
            login,name,bio,location,repos,followers,following,url = result
            return [f"Aura: Logged in as {user} ({login})",f"name : {name}",f"bio: {bio}",f"location: {location}",
                    f"repos: {repos}",f"followers: {followers}",f"following : {following}",f"url: {url}"]

    def get_weather(self,city_name):
        if 'today\'s' in city_name:
            city_name = city_name.replace('today\'s','').strip()
        if 'today' in city_name:
            city_name = city_name.replace('today','').strip()
        result = self.weather(city_name)
        if result:
            temp,desc,name = result
            return [f"Aura: Aaj {name} mai {desc} and temperature hai {temp}c ."]
        else:
            return ["Aura: Not available"]

    def location(self,a):
       return [self.get_location()]

    def mean(self,word):
        if 'what' in word:
            word = word.replace('what','').strip()
        if 'is' in word:
            word = word.replace('is','').strip()
        if 'the' in word:
            word = word.replace('the','').strip()
        if 'of' in word:
            word = word.replace('of','').strip()
        return [self.get_meaning(word)]

    def crypto(self,coin_name):
        return [self.crypto_price(coin_name.lower())]


    def exit(self):
        self.respond(self.farwell_replies())

    def command(self, user_input):
        commands = {'youtube':self.open_youtube,'date':self.date_time,'play':self.play_music,
                    'time':self.date_time,'date and time':self.date_time,'instagram':self.open_insta,
                    'joke':self.joke,'laugh':self.joke,'fact':self.get_fact,'github':self.github,
                    'weather':self.get_weather,'location':self.location,'meaning':self.mean,'crypto':self.crypto,'means':self.mean}
        for key in commands:
            if key in user_input:
                # self.respond(self.thinking_replies())
                # time.sleep(1.2)

                # self.respond(self.success_replies())
                a = user_input.replace(key,"").strip().lower()
                return  commands[key](a)
            elif user_input == 'exit':

                return self.exit()




        # if 'youtube' in user_input or 'yt' in user_input:

        #     return True
        # elif 'date' in user_input and 'time' in user_input:

        #     return True
        # elif 'time' in user_input:

        #     return True
        # elif 'date' in user_input:

        #     return True
        # elif 'chrome' in user_input:

        #     return True
        # elif 'play' in user_input and 'music' in user_input:

        #     return True
        # elif 'music' in user_input:
        #     self.type_animator("Play [Song Name]: ", False)
        #     song = input()
        #     song = song.capitalize()
        #     self.respond(self.thinking_replies())
        #     time.sleep(1.2)
        #     self.respond(f"Aura: Playing {song}...")
        #     song = song.lower()
        #     self.play_music(song)
        #     self.respond(self.success_replies())
        #     return True
        # elif 'play' == user_input:
        #     self.type_animator("What do you want to play: ", False)
        #     song = input()
        #     song = song.capitalize()
        #     self.respond(self.thinking_replies())
        #     time.sleep(1.2)
        #     self.respond(f"Aura: Playing {song}...")
        #     song = song.lower()
        #     self.play_music(song)
        #     self.respond(self.success_replies())
        #     return True
        # elif 'play' in user_input:
        #     song = user_input.replace('play', '').strip()
        #     song = song.capitalize()
        #     self.respond(self.thinking_replies())
        #     time.sleep(1.2)
        #     self.respond(f"Aura: Playing {song}...")
        #     user_input = user_input.lower()
        #     self.play_music(song)
        #     self.respond(self.success_replies())
        #     return True
        # elif 'instagram' in user_input:

        # elif 'hello' in user_input or 'hi' in user_input:
        #     self.respond(random.choice([
        #         "Aura: Hello there.",
        #         "Aura: Hi, I'm online.",
        #         "Aura: Hey, What can i do?"
        #     ]))
        # elif 'joke' in user_input or 'laugh' in user_input:

        # elif 'exit' in user_input:

        #     return False