import random

class Replies_class():
    def success_replies(self):
        success_replies1 = ["Aura: Done! Anything else?",
                            "Aura: Task completed s-uccessfully.",
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

    def greeting_replies(self, name):
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