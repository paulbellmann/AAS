from flask import Flask, request
from playsound import playsound
from gtts import gTTS
import os

app = Flask(__name__)

ip_whitelist = [
    '127.0.0.1',
    '172.30.127.12',
]

@app.route("/")
def hello_world():
    if request.remote_addr not in ip_whitelist:
        return 'Not today, bro!'

    ticket_path = os.getcwd() + '/sounds/tickets.mp3'
    alarm_path = os.getcwd() + '/sounds/ff_alarm.wav'
    text = request.args.get('text')

    myobj = gTTS(text=text, lang='de', slow=False)
    myobj.save(ticket_path)

    playsound(alarm_path)
    playsound(ticket_path)

    if os.path.isfile(ticket_path):
        os.remove(ticket_path)

    return 'Hello World'
