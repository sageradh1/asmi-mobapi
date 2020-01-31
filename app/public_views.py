from app import app
from flask import render_template

@app.route("/")
def index():
	message ="The environment is " + app.config["ENV"]
	return render_template("public_views/index.html",message=message)