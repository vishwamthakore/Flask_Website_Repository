print("hello")
for i in range(5):
	print(i)


import flask
from flask import Flask, render_template, request
import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test_database'
db = SQLAlchemy(app)


'''app -> mysql database'''
'''db -> app'''
'''db-> mysql'''

class Testing_table(db.Model):
    # sno title content

    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(120), nullable=False)



# entry = Testing_table(sno=5, title='test', content='testing connectivity')
# print('aaaaaaa')
# db.session.add(entry)
# db.session.commit()


@app.route("/")
def hello():


	l_test=[1,2,3,4,5,6]
	return render_template("index.html",l_t=l_test)


@app.route("/About")
def about():
    return "<h1>About the website! Without any template</h1>"

@app.route("/Test")
def test():
	l_test=[1,2,3,4,5,6]
	name="var"
	return render_template("test.html",l_t=l_test, name_t=name)


@app.route("/Bootstrap")
def bootstrap():
	return render_template("bootstrap.html")

@app.route('/Form', methods=['GET', 'POST'])
def hell():
	if request.method=="POST":
		nm=request.form['n']
		return "The name is {}".format(nm)

	return render_template("test_form.html")
    






app.run(debug=True, use_reloader=False)




