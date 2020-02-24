from app import app,db
from app.database.models import APIAuthKey,User
from flask import render_template, request, jsonify
from app.utils.validators import isValidPhoneNumber,isValidEmail
from app.utils.hashpassword import hash_password,verify_password
import pandas as pd
from datetime import datetime
from sqlalchemy_utils import PhoneNumber
from sqlalchemy import exists,or_,and_


@app.route("/api/create-user",methods=['POST'])
def create_user():
	# if request.headers["Content-Type"]!="application/json":
	# 	return jsonify({"message":"Invalid Request Header","data":""})

	if request.data is None:
		return jsonify({"message":"Invalid Request","data":""})		

	data = request.get_json()

	## Check Authenticity of API Request
	try:
		apikey=data["api_secrect_key"]
		if apikey is None:
			return jsonify({"message":"Unauthenticated Request","data":""})
		doesExist = APIAuthKey.query.filter_by(api_key=apikey).scalar() is not None
		if not doesExist:
			return jsonify({"message":"Unauthenticated Request","data":""})
	except Exception as err:
		print(err)
		return jsonify({"message":"API Key Parsing Error","data":str(err)})

	## Check Other Data Format
	try:
		gender=data["gender"]
		username=data["username"]
		firstname=data["firstname"]
		lastname=data["lastname"]
		dateofbirth=data["dateofbirth"]
		phonenumber=data["phonenumber"]
		email=data["email"]
		password=data["password"]

		badDataFormat=False
		if gender.upper()!="MALE" and gender.upper()!="FEMALE" and gender.upper()!="OTHER":
			badDataFormat =True

		if not isValidPhoneNumber(phonenumber):
			badDataFormat =True

		if not isValidEmail(email):
			badDataFormat =True

		dateofbirthDate = pd.to_datetime(dateofbirth)	

		if badDataFormat == True:
			return jsonify({"message":"Invalid Data Format","data":""})
	except Exception as err:
		return jsonify({"message":"Invalid Data Format","data":""})

	try:
		doesUserMatch = db.session.query(exists().where(or_(User.email==email,User.username==username,User.phone_number==phonenumber))).scalar()
		if doesUserMatch:
			doesUserEmailMatch = db.session.query(exists().where(User.email==email)).scalar()
			if doesUserEmailMatch:
				return jsonify({"message":"Duplicate Email","data":""})

			doesUserPhoneMatch = db.session.query(exists().where(User.phone_number==phonenumber)).scalar()
			if doesUserPhoneMatch:
				return jsonify({"message":"Duplicate PhoneNumber","data":""})

			doesUsernameMatch = db.session.query(exists().where(User.username==username)).scalar()
			if doesUsernameMatch:
				return jsonify({"message":"Duplicate Username","data":""})
	except Exception:
		return jsonify({"message":"Database Access Error","data":""})

	# Inserting into database
	try:
		hashpassword=hash_password(password)
		user = User(gender=gender,first_name=firstname,last_name=lastname,username=username,email=email,phone_number=phonenumber,date_of_birth=dateofbirthDate,created_datetime=datetime.utcnow(),password_hash=hashpassword)
		db.session.add(user)
		db.session.commit()

		result={}
		result["userid"]=str(user.id)
		result["gender"]=str(user.gender)
		result["username"]=str(user.username)
		result["firstname"]=str(user.first_name)
		result["lastname"]=str(user.last_name)
		result["dateofbirth"]=str(user.date_of_birth)
		result["created_datetime"]=str(user.created_datetime)
		result["phonenumber"]=str(user.phone_number)
		result["email"]=str(user.email)

		return jsonify({"message":"Success","data":result})
	except Exception as err:
		print(err)
		return jsonify({"message":"Database Storing Error","data":""})


@app.route("/api/user-login",methods=['GET','POST'])
def user_login():
	# if request.headers["content-type"]!="application/json" or request.headers["Content-Type"]!="application/json":
	# 	return jsonify({"message":"Invalid Request Header","data":""})

	if request.data is None:
		return jsonify({"message":"Invalid Request","data":""})		

	data = request.get_json()

	## Check Authenticity of API Request
	try:
		apikey=data["api_secrect_key"]
		if apikey is None:
			return jsonify({"message":"Unauthenticated Request","data":""})
		doesExist = APIAuthKey.query.filter_by(api_key=apikey).scalar() is not None
		if not doesExist:
			return jsonify({"message":"Unauthenticated Request","data":""})
	except Exception as err:
		return jsonify({"message":"API Key Parsing Error","data":""})

	## Check Other Data Format
	try:
		email=data["email"]
		password=data["password"]

		badDataFormat=False
		
		if not isValidEmail(email):
			badDataFormat =True

		if badDataFormat == True:
			return jsonify({"message":"Invalid Data Format","data":""})
	except Exception as err:
		return jsonify({"message":"Invalid Data Format","data":""})

	try:
		user = User.query.filter_by(email=email).first()
		if user is None:
			return jsonify({"message":"The email does not exist.","data":""})
		isPasswordCorrect = verify_password(user.password_hash,password)
		if not isPasswordCorrect:
			return jsonify({"message":"Invalid Credentials.","data":""})
	except Exception as err:
		return jsonify({"message":err,"data":""})
		# return jsonify({"message":"Database Access Error","data":""})

	# Inserting into database
	try:
		user.is_active=True
		print(user.is_active)
		db.session.commit()

		result={}
		result["userid"]=str(user.id)
		result["gender"]=str(user.gender)
		result["username"]=str(user.username)
		result["firstname"]=str(user.first_name)
		result["lastname"]=str(user.last_name)
		result["dateofbirth"]=str(user.date_of_birth)
		result["created_datetime"]=str(user.created_datetime)
		result["phonenumber"]=str(user.phone_number)
		result["email"]=str(user.email)

		return jsonify({"message":"Success","data":result})
	except Exception as err:
		print(err)
		return jsonify({"message":"Database Storing Error","data":""})



@app.route("/api/user-logout",methods=['GET','POST'])
def user_logout():
	# if request.headers["Content-Type"]!="application/json":
	# 	return jsonify({"message":"Invalid Request Header","data":""})

	if request.data is None:
		return jsonify({"message":"Invalid Request","data":""})		

	data = request.get_json()

	## Check Authenticity of API Request
	try:
		apikey=data["api_secrect_key"]
		if apikey is None:
			return jsonify({"message":"Unauthenticated Request","data":""})
		doesExist = APIAuthKey.query.filter_by(api_key=apikey).scalar() is not None
		if not doesExist:
			return jsonify({"message":"Unauthenticated Request","data":""})
	except Exception as err:
		return jsonify({"message":"API Key Parsing Error","data":""})

	## Check Other Data Format
	try:
		email=data["email"]
		userid=data["userid"]

		badDataFormat=False
		
		if not isValidEmail(email):
			badDataFormat =True

		if badDataFormat == True:
			return jsonify({"message":"Invalid Data Format","data":""})
	except Exception as err:
		return jsonify({"message":"Invalid Data Format","data":""})

	try:
		user = User.query.get(userid)
		if (user is None) or (not user.email==email):
			return jsonify({"message":"Invalid Data","data":""})

	except Exception as err:
		print(err)
		return jsonify({"message":"Database Access Error","data":""})

	# Inserting into database
	try:
		user.is_active=False
		print(user.is_active)
		db.session.commit()

		result={}
		result["userid"]=user.id
		result["phonenumber"]=str(user.phone_number)
		result["email"]=str(user.email)

		return jsonify({"message":"Success","data":result})
	except Exception as err:
		print(err)
		return jsonify({"message":"Database Storing Error","data":""})
 

# @app.route("/api/test",methods=['POST'])
# def test():
# 	doesUserMatch = db.session.query(exists().where(and_(User.email=="user@domain.com",User.username=="test"))).scalar()
# 	if doesUserMatch:
# 		doesUserEmailMatch = db.session.query(exists().where(User.email=="user@domain.com")).scalar()
# 		if doesUserEmailMatch:
# 			return jsonify({"message":"Duplicate Email","data":""})

# 		doesUserPhoneMatch = db.session.query(exists().where(User.phone_number=="user@domain.com")).scalar()
# 		if doesUserPhoneMatch:
# 			return jsonify({"message":"Duplicate PhoneNumber","data":""})

# 		doesUsernameMatch = db.session.query(exists().where(User.username=="user@domain.com")).scalar()
# 		if doesUsernameMatch:
# 			return jsonify({"message":"Duplicate Username","data":""})


# 	# exists = db.session.query(User.id).filter_by(name='davidism').scalar() is not None

# 	# doesExist = User.query.filter_by(and_(email="user@domain.com")).scalar() is not None
# 	# if not doesExist:
# 	# 	return jsonify({"message":"Unauthenticated Request",data:""})
# 	print(ret)
# 	return jsonify({"processing has ":str(ret),"data":""})