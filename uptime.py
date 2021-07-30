from flask import Flask
from threading import Thread


app = Flask("")


@app.route("/")
def home():
    return "I am currently online!"

def run():
    app.run(host = "0.0.0.0", port = 8080)

def online():
    start = Thread(target = run)
    start.start()