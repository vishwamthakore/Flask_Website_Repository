print("hello")
for i in range(5):
	print(i)


import flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/About")
def about():
    return "About the website!"

app.run()




