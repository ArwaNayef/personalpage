from flask import Flask, render_template, request
import dataset
import random
app = Flask(__name__)

#db = dataset.connect("postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4")
#user_table = db["arwa_user"]


#user_table.insert(dict(firstname= "hala", lastname="barka" , message="hello"))
#user_table.insert(dict(firstname= "Arwa", lastname="nayef", message="hi"))
#
#for user in user_table:
#		print (";firstame"+ ";lastname"+";message"+";gender")


#print(db.tables)
#print(table.colums)



@app.route("/")

def home_page():
	fourtunes= ["You will eat lots of bread",
	"you will find a treasure","you will be a doctor",
	"you will marry very soon ",
	"someone loves you very much"]
	
	return render_template("index.html", qoute=random.choice(fourtunes))
		
@app.route("/wecode")
def wecodee ():
	return render_template("aboutme.html")


#@app.route("/access")
#def access ():
#	return render_template("access.html")


@app.route("/contactme")
def contactme ():
	return render_template("contactme.html")

@app.route("/contactme_response",methods= ['POST'])
def contactmeres():
	user_firstname= request.form["firstname"]
	user_lastname= request.form["lastname"]
	user_message= request.form["messege"]
	user_gender= request.form["gender"]
	#user_table.insert(dict(firstname= user_firstname , lastname= user_lastname, messege=user_message))
	#return user_table.findone(firstame="hala")
	


	return render_template("form-data.html", firstname=user_firstname, 
		lastname=user_lastname,message= user_message , gender=user_gender)



if __name__ =="__main__":
	app.run()
