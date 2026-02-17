import pyjokes
import time
import sys
import webbrowser
import random
import os
from datetime import datetime
import pywhatkit
import pyttsx3
import speech_recognition as sr
class Text_Animator:
           def type_animator(self,text,new_line):
               for ch in text:
                    if ch == '.':
                         sys.stdout.write(ch)
                         sys.stdout.flush()
                         time.sleep(0.8)
                    elif ch == '\n':
                         sys.stdout.write(ch)
                         sys.stdout.flush()
                         time.sleep(0.08)
                    elif ch == ',':
                         sys.stdout.write(ch)
                         sys.stdout.flush()
                         time.sleep(0.25)
                    elif ch == '?':
                         sys.stdout.write(ch)
                         sys.stdout.flush()
                         time.sleep(0.7)
                    elif ch == '!':
                         sys.stdout.write(ch)
                         sys.stdout.flush()
                         time.sleep(0.4)
                    elif ch == ' ':
                         sys.stdout.write(ch)
                         sys.stdout.flush()
                         time.sleep(0.01)
                    else:
                         sys.stdout.write(ch)
                         sys.stdout.flush()
                         time.sleep(0.04)
               if new_line == True:
                    sys.stdout.write('\n')
                    sys.stdout.flush()
class Replies_class(Text_Animator):
     def success_replies(self):
          success_replies1 = ["Aura: Done! Anything else?",
    "Aura: Task completed successfully.",
    "Aura: All set.",
    "Aura: Mission accomplished.",
    "Aura: That worked perfectly.",
    "Aura: Consider it done.",
    "Aura: Execution successful.",
    "Aura: Finished. What next?",
    "Aura: Done and ready for next command.",
    "Aura: Operation successful."]
          reply = random.choice(success_replies1)
          return reply
     def thinking_replies(self):
          thinking_replies1 = [
    "Aura: Let me think...",
    "Aura: Processing your request...",
    "Aura: Working on it...",
    "Aura: Analyzing command...",
    "Aura: One moment please...",
    "Aura: Checking that for you...",
    "Aura: Give me a second..."]
          reply = random.choice(thinking_replies1)
          return reply
     def casual_replies(self):
           casual_replies1 = [
    "Aura: I'm listening.",
    "Aura: Go on...",
    "Aura: Interesting.",
    "Aura: Tell me more.",
    "Aura: I'm here.",
    "Aura: What else can I do?",
    "Aura: Sounds good."]
           reply = random.choice(casual_replies1)
           return reply
     def Unknown_replies(self):
            unknown_replies1 = [
    "Aura: I didn't understand that.",
    "Aura: Hmm... try saying it differently.",
    "Aura: That command is unfamiliar to me.",
    "Aura: Can you rephrase that?",
    "Aura: I'm still learning that one.",
    "Aura: Command not recognized."]
            reply = random.choice(unknown_replies1)
            return reply
     def greeting_replies(self,name):
          greetings = [
    f"Aura: Hello, {name}.",
    f"Aura: Hi there {name}.",
    "Aura: Good to see you again.",
    "Aura: Ready when you are.",
    f"Aura: Hey {name}, how can I help?"]
          reply = random.choice(greetings)
          return reply
     def farwell_replies(self):
               farewell_replies = [
    "Aura: Goodbye.",
    "Aura: See you soon.",
    "Aura: Shutting down. Take care.",
    "Aura: Session ended.",
    "Aura: Until next time.",
    "Aura: Aura signing off."]
               reply = random.choice(farewell_replies)
               return reply
class Aura(Replies_class):
     def __init__(self):
           self.recognizer = sr.Recognizer()
     def aura_say(self,text,new_line):
           self.type_animator(text,new_line)
           text1 = text.replace('Aura:','')
           engine = pyttsx3.init()
           voices = engine.getProperty('voices')
           engine.setProperty('voice',voices[1].id) 
           engine.stop()
           engine.say(text1)
           engine.runAndWait()
     def aura_ears2(self):
           r = self.recognizer

           with sr.Microphone() as source:
               self.aura_say(random.choice([
    "Aura: I'm listening...",
    "Aura: Go ahead.",
    "Aura: Speak now.",
    "Aura: Waiting for your command.",
    "Aura: Say something.",
    "Aura: What can I do for you?",
    "Aura: Tell me.",
    "Aura: I'm ready.",
    "Aura: Your move.",
    "Aura: Yes?",
    "Aura: Awaiting instructions.",
    "Aura: Command received. Speak.",
    "Aura: Systems listening.",
    "Aura: Voice channel open.",
    "Aura: Standing by.",
    "Aura: I'm all ears.",
    "Aura: Talk to me.",
    "Aura: I'm here.",
    "Aura: What's on your mind?",
    "Aura: Ready when you are.",
    "Aura: Don't be shy, say it.",
    "Aura: Mic is yours.",
    "Aura: Waiting patiently...",
    "Aura: Listening carefully.",
    "Aura: Go on, I'm paying attention.",
    "Aura: Say the word.",
    "Aura: I'm awake.",
    "Aura: Ready for your command.",
    "Aura: Input channel active.",
    "Aura: Listening mode enabled."
]), True)
               time.sleep(0.6)
               r.adjust_for_ambient_noise(source, duration=0.5)
               audio = r.listen(source)

           try:
               text = r.recognize_google(audio).lower()
               self.type_animator(f"You: {text}", True)
               return self.command(text, 'voice')

           except:
               self.aura_say("Sorry, couldn't understand.", True)
               return True
     def respond(self,text,mode):
           if mode == 'text':
                 self.type_animator(text,True)
           else:
                 self.aura_say(text,True)
     def open_insta(self):
          webbrowser.open("https://instagram.com")
     def open_youtube(self):
          webbrowser.open("https://youtube.com")
     def open_chrome(self):
           os.system("start chrome")
     def play_music(self,link):
           pywhatkit.playonyt(link)        
     def command(self,user_input,textorvoice):
          if 'youtube' in user_input or 'yt' in user_input:
               self.respond(self.thinking_replies(),textorvoice)
               time.sleep(1.2)
               self.respond("Aura: Opening Youtube...",textorvoice)
               self.open_youtube()
               self.respond(self.success_replies(),textorvoice)
               return True
          elif 'date' in user_input and 'time' in user_input:
               date12 = datetime.now().strftime("%d-%m-%y")
               time_now = datetime.now().strftime("%I:%M %p")
               self.respond(self.thinking_replies(),textorvoice)
               time.sleep(1.2)
               self.respond(f"Aura: Today is {date12}. ",textorvoice)
               self.respond(f"Aura: Current time is {time_now} ",textorvoice)
               self.respond(self.success_replies(),textorvoice)
               return True
          elif 'time' in user_input:
               time_now = datetime.now().strftime("%I:%M %p")
               self.respond(self.thinking_replies(),textorvoice)
               time.sleep(1.2)
               self.respond(f"Aura: Current time is {time_now}. ",textorvoice)
               self.respond(self.success_replies(),textorvoice)
               return True
          elif 'date' in user_input:
               date12 = datetime.now().strftime("%d-%m-%y")
               self.respond(self.thinking_replies(),textorvoice)
               time.sleep(1.2)
               self.respond(f"Aura: Today is {date12}. ",textorvoice)
               self.respond(self.success_replies(),textorvoice)
               return True
          elif 'chrome' in user_input:
               self.respond(self.thinking_replies(),textorvoice)
               time.sleep(1.2)
               self.respond("Aura: Opening Chrome...",textorvoice)
               self.open_chrome()
               self.respond(self.success_replies(),textorvoice)
               return True
          elif 'play' in user_input and 'music' in user_input:
               self.type_animator("Play [Song Name]: ",False)
               song = input()
               song = song.capitalize()
               self.respond(self.thinking_replies(),textorvoice)
               time.sleep(1.2)
               self.respond(f"Aura: Playing {song}...",textorvoice)
               song = song.lower()
               self.play_music(song)
               self.respond(self.success_replies(),textorvoice)
               return True
          elif 'music' in user_input:
               self.type_animator("Play [Song Name]: ",False)
               song = input()
               song = song.capitalize()
               self.respond(self.thinking_replies(),textorvoice)
               time.sleep(1.2)
               self.respond(f"Aura: Playing {song}...",textorvoice)
               song = song.lower()
               self.play_music(song)
               self.respond(self.success_replies(),textorvoice)
               return True
          elif 'play' == user_input:
               self.type_animator("What do you want to play: ",False)
               song = input()
               song = song.capitalize()
               self.respond(self.thinking_replies(),textorvoice)
               time.sleep(1.2)
               self.respond(f"Aura: Playing {song}...",textorvoice)
               song = song.lower()
               self.play_music(song)
               self.respond(self.success_replies(),textorvoice)
               return True
          elif 'play' in user_input:
               song = user_input.replace('play','').strip()
               song = song.capitalize()
               self.respond(self.thinking_replies(),textorvoice)
               time.sleep(1.2)
               self.respond(f"Aura: Playing {song}...",textorvoice)
               user_input = user_input.lower()
               self.play_music(song)
               self.respond(self.success_replies(),textorvoice)
               return True
          elif 'instagram' in user_input:
               self.respond(self.thinking_replies(),textorvoice)
               time.sleep(1.2)
               self.respond("Aura: Opening Instagram...",textorvoice)
               self.open_insta()
               self.respond(self.success_replies(),textorvoice)
          elif 'hello' in user_input or 'hi' in user_input:
               self.respond(random.choice([
                    "Aura: Hello there.",
                    "Aura: Hi, I'm online.",
                    "Aura: Hey, What can i do?"
               ]),textorvoice)
          elif 'joke' in user_input or 'laugh' in user_input:
               self.respond(pyjokes.get_joke('en','all'),textorvoice)
          elif 'exit' in user_input:
               self.respond(self.farwell_replies(),textorvoice)
               return False
aura1 = Aura()
booting_text = '''Booting Aura...
Initializing modules...
Loading personality core...
System Online.'''
aura1.type_animator(booting_text,True)
aura1.type_animator("Enter your name: ",False)
name = input()
aura1.aura_say(aura1.greeting_replies(name),True)
a = input("Press enter for voice mode or press any key for type mode")
if a == '':
      while True:
          flag1 = aura1.aura_ears2()
          time.sleep(0.2)
          if flag1 == False:
               break
          else: 
               continue      
else:      
     while True:
          aura1.type_animator("You: ",False)
          user_input = input()
          user_input = user_input.lower()
          flag1 = aura1.command(user_input,'text')
          if flag1 == False:
               break
          else: 
               continue