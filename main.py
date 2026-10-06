from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hi, I am Eden from Enterprise Web Dev!</h1>"

@app.route("/name")
def name():
    return "<h1>Hi, I am Eden from Enterprise Web Dev!</h1>"
