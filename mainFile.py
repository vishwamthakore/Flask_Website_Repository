print("hello")
for i in range(5):
	print(i)


import flask
from flask import Flask, render_template, request
import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test_database'
# app.jinja_env.cache={}
# app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.config['SECRET_KEY']="55a144e7c56273364b0eb3ba25ce3b6"
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
		msg=request.form['q']

		entry = Testing_table(sno=6, title=nm, content=msg)
		print("wwww")
		db.session.add(entry)
		db.session.commit()


		return "The name is {}".format(nm)

	return render_template("test_form.html")
    



class Upload_table(db.Model):
    # sno title content
    srno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)


@app.route('/UploadForm', methods=['GET', 'POST'])
def upload():
	if request.method=="POST":
		fn=request.form["p"]
		ln=request.form["q"]

		row= Upload_table(srno=2, title=fn, description=ln)
		print('qqqqqqq')
		db.session.add(row)
		db.session.commit()

		return "<h1>Firstname and Lastname are {}</h1>".format(fn)



	return render_template("upload_form.html")



@app.route("/Output")
def fetch_from_db():

	row1=Testing_table.query.first()

	rows=Testing_table.query.all()
	return render_template("output.html",r1=row1, r=rows)


@app.route("/jk")
def j():
	return 'jqqqqqqqq'




app.run(debug=True, use_reloader=False)

# , host='0.0.0.0'





