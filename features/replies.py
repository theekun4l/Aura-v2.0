import random


class Replies_class():
    def success_replies(self):
        reply = random.choice(["Aura: Done! Anything else?",
                            "Aura: Task completed s-uccessfully.",
                            "Aura: All set.",
                            "Aura: Mission accomplished.",
                            "Aura: That worked perfectly.",
                            "Aura: Consider it done.",
                            "Aura: Execution successful.",
                            "Aura: Finished. What next?",
                            "Aura: Done and ready for next command.",
                            "Aura: Operation successful."])
        return reply


    def thinking_replies(self):
        reply = random.choice([
            "Aura: Let me think...",
            "Aura: Processing your request...",
            "Aura: Working on it...",
            "Aura: Analyzing command...",
            "Aura: One moment please...",
            "Aura: Checking that for you...",
            "Aura: Give me a second..."])
        return reply

    def greeting_replies(self):
        reply = random.choice([
            "Aura: Hello there.",
            "Aura: Hi there.",
            "Aura: Good to see you again.",
            "Aura: Ready when you are.",
            "Aura: Hey, how can I help?",
            "Aura: Welcome back.",
            "Aura: Hey! What's up?",
            "Aura: Hello! How are you?",
            "Aura: Hi! What can I do for you?",
            "Aura: Hey there!",
            "Aura: Nice to see you.",
            "Aura: Hello! What are we working on today?"
        ])
        return reply

    def farwell_replies(self):
        reply = random.choice([
            "Aura: Goodbye.",
            "Aura: See you soon.",
            "Aura: Shutting down. Take care.",
            "Aura: Session ended.",
            "Aura: Until next time.",
            "Aura: Aura signing off."])
        return reply