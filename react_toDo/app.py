from flask import Flask
app = Flask(__name__)

@app.route("/")
def world():
    return " World!"

@app.route('/hello')
def hello():
    return 'Hello, World'
