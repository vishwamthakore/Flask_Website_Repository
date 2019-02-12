print("hello")
for i in range(5):
	print(i)


import flask
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():


	l_test=[1,2,3,4,5,6]
	return render_template("index.html",l_t=l_test)


@app.route("/About")
def about():
    return "<h1>About the website! Without any template<h1>"

@app.route("/Test")
def test():
	name="var"
	return render_template("test.html", name_t=name)

@app.route("/Bootstrap")
def bootstrap():
	return render_template("bootstrap.html")





app.run(debug=True)




