import time

class Text_Animator():
    def type_animator(self, text):
        for word in text.split():
            yield word + " "
            time.sleep(0.05)