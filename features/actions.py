import webbrowser,time,random,pyjokes,os  #,pywhatkit
from features.utils import Text_Animator
from features.replies import Replies_class
from datetime import datetime
from LLM.llm import ask_llm
class Aura(Text_Animator,Replies_class):

    def open_insta(self):
        webbrowser.open("https://instagram.com")
        return None,None


    def open_youtube(self):
        webbrowser.open("https://youtube.com")
        return None,None

    def open_chrome(self):
        os.system("start chrome")
        return None,None


    # def play_music(self,music):
    #         pywhatkit.playonyt(music)

    def date_time(self):
            date12 = datetime.now().strftime("%d-%m-%y")
            time_now = datetime.now().strftime("%I:%M %p")
            return f"Aura: Today is {date12}. " , f"Aura: Current time is {time_now} "
    def joke(self):
        return pyjokes.get_joke('en', 'all'),None

    def exit(self):
        self.respond(self.farwell_replies())

    def command(self, user_input):
        commands = {'youtube':self.open_youtube,'date':self.date_time,'time':self.date_time,'date and time':self.date_time,'instagram':self.open_insta,'joke':self.joke,'laugh':self.joke}
        for key in commands:
            flag = False #if its not in command list
            if key in user_input:
                flag = True
                break

        if flag:
            a,b = commands[key]()
            return a,b,True
        else:
            msg = ask_llm(user_input)
            return msg,False,False



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