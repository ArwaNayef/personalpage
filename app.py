from flask import Flask, render_template
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


if __name__ =="__main__":
	app.run()
