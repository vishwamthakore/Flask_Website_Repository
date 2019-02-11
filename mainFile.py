print("hello")
for i in range(5):
	print(i)


import flask
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/About")
def about():
    return "<h1>About the website! Without any template<h1>"

@app.route("/Test")
def test():
	name="var"
	return render_template("test.html", name_t=name)



app.run(debug=True)




