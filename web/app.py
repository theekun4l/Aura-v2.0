from flask import Flask, render_template, request
from features.actions import Aura
import time

aura = Aura()

app = Flask(__name__)
chat_history = []
@app.route('/',methods=['GET','POST'])
def home():
    global chat_history

    if request.method == 'POST':
        user_input = request.form['msg']
        bot_reply = aura.command(user_input)
        chat_history.append(('You',user_input))
        chat_history.append(('Aura',bot_reply))
        time.sleep(1)
    return render_template("index.html",chat=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
