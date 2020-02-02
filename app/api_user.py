from app import app,db
from flask import render_template, request, jsonify

@app.route("/api/create-user",methods=['POST'])
def create_user():
	if request.headers["Content-Type"]!="application/json":
		return jsonify({"message":"Invalid Request Header","data":""})

	# data = request.get_json()
	# apikey=data["api_secrect_key"]
	# # if !apikey:
	# 	return jsonify({"message":"Invalid Request",data:""})
	# try:		
	# 	user = User(id=request.form.get("id"), username=request.form.get("username"),email=request.form.get("email"))
	# 	db.session.add(user)
	# 	db.session.commit()
	# catch:
	# 	return jsonify({"message":"Invalid Request",data:""})
	return jsonify(request.headers["Content-Type"])

 