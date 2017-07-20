from flask import Flask, render_template, request

import random
app = Flask(__name__)

@app.route("/")#homepag

def home_page():
	fourtunes= ["You will eat lots of bread",
	"you will find a treasure","you will be a doctor",
	"you will marry very soon ",
	"someone loves you very much"]
	
	return render_template("index.html", qoute=random.choice(fourtunes))
		
@app.route("/wecode")
def wecodee ():
	return render_template("aboutme.html")


@app.route("/access")
def access ():
	return render_template("access.html")


@app.route("/contactme")
def contactme ():
	return render_template("contactme.html")

@app.route("/contactme_response",methods= ['POST'])
def contactmeres():
	user_firstname= request.form["firstname"]
	user_lastname= request.form["lastname"]
	user_message= request.form["messege"]
	user_gender= request.form["gender"]
	#return user_firstname+ " " +user_lastname+ " " +user_messege + user_gender
	return render_template("form-data.html", firstname=user_firstname, 
		lastname=user_lastname,user_message=message , user_gender=gender)

if __name__ =="__main__":
	app.run()
