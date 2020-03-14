from app import app,db
from app.database.models import APIAuthKey,User,VideoPost
from flask import render_template, request, jsonify
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.utils import secure_filename
import os
from datetime import datetime

def isVideoNameAllowed(filename):
    # We only want files with a . in the filename
    if not "." in filename:
        return False
    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]
    # Check if the extension is in ALLOWED_VIDEO_EXTENSIONS
    if ext.lower() in app.config["ALLOWED_VIDEO_EXTENSIONS"]:
        return True
    else:
        return False

@app.route("/api/post-video",methods=['POST'])
def post_video():
	_videoUploadStartingTime=datetime.utcnow()
	startingdt_string = _videoUploadStartingTime.strftime("%Y%m%d%H%M%S")

	# if "multipart/form-data" not in request.headers["Content-Type"]:
	# 	return jsonify({"message":"Invalid Request Header","data":""})

	data = dict(request.form)

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

	#Make sure data is a number
	try:
		userid=int(data["userid"])
		caption=data["caption"]
		audio_info=data["audio_info"]
		givenvideosizeinkb=int(data["videosizeinkb"])
	except Exception as err:
		return jsonify({"message":"Invalid Data Format","data":""})

	if givenvideosizeinkb>=app.config["MAX_VIDEO_FILESIZE"]:
		return jsonify({"message":"Filesize limit exceeded","data":""})


	user = User.query.filter_by(id=userid).first()
	if user is None:
		return jsonify({"message":"Invalid User Request","data":""})
	if not user.is_active:
		return jsonify({"message":"Invalid User Request","data":""})

	# check if the post request has the file part
	if ('videofile' not in request.files):
	    return jsonify({"message":"Invalid Data Format","data":""})
	#file = request.files['file']
	videofile = request.files['videofile']
	if not isVideoNameAllowed(secure_filename(videofile.filename)):
	    return jsonify({"message":"Invalid Request Header","data":""})


	_videostorageLocation = app.config["VIDEO_UPLOADS_FOLDER"]
	_videofilename= videofile.filename

	_basename=startingdt_string+_videofilename.split('.')[0]
	_extension=_videofilename.split('.')[1]

	videofile.save(os.path.join(_videostorageLocation, startingdt_string+videofile.filename))

	_videoUploadCompletedTime=datetime.utcnow()

	try:
		_uploadedVideoPost=VideoPost(filename = _basename, extension = _extension,storagelocation = _videostorageLocation,upload_started_time = _videoUploadStartingTime,upload_completed_time = _videoUploadCompletedTime,caption=caption,audio_info=audio_info,author=user)
		db.session.add(_uploadedVideoPost)
		db.session.commit()
	except Exception as err:
		return jsonify({"message":"Database Access Error","data":""})

	result={}
	result["videoid"]=str(_uploadedVideoPost.id)
	result["posterid"]=str(user.id)	
	result["posterusername"]=str(user.username)
	result["videofilename"]=str(_uploadedVideoPost.filename)	
	result["upload_started_time"]=str(_uploadedVideoPost.upload_started_time)
	result["upload_completed_time"]=str(_uploadedVideoPost.upload_completed_time)
	
	return jsonify({"message":"Success","data":result})





@app.route("/api/newsfeed-videoposts",methods=['POST'])
def newsfeed_videoposts():
	if request.data is None:
		return jsonify({"message":"Invalid Request","data":""})		

	data = request.get_json()

	## Check Authenticity of API Request
	try:
		apikey=data["api_secret_key"]
		if apikey is None:
			return jsonify({"message":"Unauthenticated Request","data":""})
		doesExist = APIAuthKey.query.filter_by(api_key=apikey).scalar() is not None
		if not doesExist:
			return jsonify({"message":"Unauthenticated Request","data":""})
	except Exception as err:
		return jsonify({"message":"API Key Parsing Error","data":str(err)})

	#Make sure data is a number
	try:
		userid=int(data["userid"])
		lastvideoid=int(data["lastvideoid"])
	except Exception as err:
		return jsonify({"message":"Invalid Data Format","data":""})

	user = User.query.filter_by(id=userid).first()
	if (user is None):
		return jsonify({"message":"Invalid User Request","data":""})
	if not user.is_active:
		return jsonify({"message":"Invalid User Request","data":""})

	try:
		latestvideoPost=[]
		if lastvideoid==-1:
			latestvideoPostList=VideoPost.query.order_by(VideoPost.id.desc()).limit(10)
		else:
			latestvideoPostList=VideoPost.query.filter(VideoPost.id<lastvideoid).limit(10)

		resultList=[]
		for eachvideopost in latestvideoPostList:
			resultObject={}
			resultObject["videoid"]=eachvideopost.id
			resultObject["videourl"]=app.config["BASE_URL"]+"/static/video/uploaded/"+eachvideopost.filename+"."+eachvideopost.extension
			resultObject["caption"]=eachvideopost.caption
			resultObject["audio_info"]=eachvideopost.audio_info
			resultObject["poster_id"]=eachvideopost.user_id
			poster = User.query.filter_by(id=eachvideopost.user_id).first()
			if (user is None):
				resultObject["poster_email"]=""
			else:
				resultObject["poster_email"]=poster.email

			print(resultObject)
			resultList.append(resultObject.copy())

	except Exception as err:
		print(err)
		return jsonify({"message":"Database Access Error","data":""})

	result=resultList
	
	return jsonify({"message":"Success","data":result})



