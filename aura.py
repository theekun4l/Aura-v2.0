from features.actions import Aura

aura1 = Aura()
# booting_text = '''Booting Aura...
# Initializing modules...
# Loading personality core...
# System Online.'''
# aura1.type_animator(booting_text,True)
aura1.type_animator("Enter your name: ",False)
name = input()
aura1.type_animator(aura1.greeting_replies(name),True)
while True:
          aura1.type_animator("You: ",False)
          user_input = input()
          user_input = user_input.lower()
          flag1 = aura1.command(user_input)
          if flag1 == False:
               break
          else: 
               continue