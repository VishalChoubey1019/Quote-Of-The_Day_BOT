#YOU CAN NOW KEEP YOUR BOT RUNNING 24*7 WITH THIS TINY PIECE OF CODE ON ANY HOSTING WEBSITE LIKE UptimeRobot

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
    
