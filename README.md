# ASMI MOBILE API
## Version 1.0.0

###### Current Secret API key is c6fd54b7f4ad40ff9f1f75ab1ac77b10 

###### Since the api key or API baseurl might change throught the process, it is advisable to code in a standard config file (global/static config variable) structure so that whenever there is a change in API from server side, just changing api key or baseurl in one place in the code side would work as well.

## API Documentation

### Latest change : 
	- Added jsonurl field to 2.bNewsfeed VideoPost


### Defaults:
	By default, these REST APIs will have the following usages and error responses.
	If unstated, these guidelines are applicable for all the apis.

* **Type:** POST
* **Request Header:**
	 contentType: 'application/json'
* **Request Body:**
	```javascript
		{
			"api_secrect_key":"your valid secret key",
			"otherkey":"valuepairs"
		}
	```

* **Response:**
	* Success:
	```javascript
		{
			"message":"Success",
			"data": somedata
		}
	```
	* Error:
		When Request header is other than "application/json":
		```javascript
			{
				"message": "Invalid Request Header",
			  	"data": ""
			}
		```
		When api_secrect_key is invalid:
		```javascript
			{
				"message": "Unauthenticated Request",
				"data": ""
			}
		```
		When the data are in invalid format:
		```javascript
			{
				"message": "Invalid Data Format",
				"data": ""
			}
		```
		When there is problem while storing information in database:
		```javascript
			{
				"message": "Database Storing Error",
				"data": ""
			}
		```
		When there is a problem in the server and database side:
		```javascript
			{
				"message": "Database Access Error",
				"data": ""
			}
		```



### 1.a Create User
* **Url:** 18.221.137.201:8080/api/create-user
* **Request Header:**
	 contentType: 'application/json'
* **Request Body:**
	```javascript
		{
			"api_secrect_key":"your valid secret key",
			"gender":"male/female/other"
			"username":"username",
			"firstname":"firstname",
			"lastname":"lastname",
			"dateofbirth":"1995-10-24",(<== This format is crucial)
			"phonenumber":"9876543210",
			"email":"user@domain.com",
			"password":"somepassword"
		}
	```

* **Response:**
	* Success:
	```javascript
		{
			"message":"Success",
			"data":{
				"userid":"32",
				"gender":"male/female/other",
				"username":"username",
				"firstname":"firstname",
				"lastname":"lastname",
				"dateofbirth":"DateTimedata",
				"created_datetime":"createdTimedata"
				"phonenumber":"9876543210",
				"email":"user@domain.com"
			}
		}
	```
	* Error:
		When dataofbirth,phonenumber or email are invalid:
		```javascript
			{
				"message": "Invalid Data Format",
				"data": ""
			}
		```
		When the email already exists in the database:
		```javascript
			{
				"message": "Duplicate Email",
				"data": ""
			}
		```
		When the phone number is already registered in the database:
		```javascript
			{
				"message": "Duplicate PhoneNumber",
				"data": ""
			}
		```
		When the username already exists in the database:
		```javascript
			{
				"message": "Duplicate Username"
			}
		```


### 1.b User Login
* **Type:** GET
* **Url:** 18.221.137.201:8080/api/user-login
* **Request Header:**
	 contentType: 'application/json'
* **Request Body:**
	```javascript
		{
			"api_secrect_key":"your valid secret key",
			"email":"desktop1@domain.com",
			"password":"somepassword"
		}
	```

* **Response:**
	* Success:
	```javascript
		{
			"message":"Success",
			"data":{
				"userid":"32",
				"gender":"male/female/other",
				"username":"username",
				"firstname":"firstname",
				"lastname":"lastname",
				"dateofbirth":"DateTimedata",
				"created_datetime":"createdTimedata"
				"phonenumber":"9876543210",
				"email":"user@domain.com"
			}
		}
	```
	* Error:
		When the email doesnot exist:
		```javascript
			{
				"message": "The email does not exist",
				"data": ""
			}
		```
		When email and password are invalid:
		```javascript
			{
				"message": "Invalid Credentials",
				"data": ""
			}
		```

### 1.c User Logout
* **Type:** GET
* **Url:** 18.221.137.201:8080/api/user-logout
* **Request Header:**
	 contentType: 'application/json'
* **Request Body:**
	```javascript
		{
			"api_secrect_key":"your valid secret key",
			"email":"user1@domain.com",
			"userid":21
		}
	```

* **Response:**
	* Success:
	```javascript
			{
			  "data": {
			    "email": "user1@domain.com",
			    "phonenumber": "9876543311",
			    "userid": 2
			  },
			  "message": "Success"
			}
	```
	* Error:
		When the email or userid are invalid:
		```javascript
			{
			  "data": "",
			  "message": "Invalid Data"
			}
		```





### 2.a Post Video
* **Type:** POST
* **Url:** 18.221.137.201:8080/api/post-video
* **Request Header:**
	 contentType: 'multipart/form-data'
* **Request Body:**
	Please keep in mind that it is not json format request.
	In multipart request, the whole file along with other side data can appear in a key-pair value form as well.
	```javascript
		KEY					VALUE
		videofile		= Actualfile		
		api_secrect_key	= "your valid secret key"
		videosizeinkb	= 111000 
		userid			= 1         (<=== The Poster ID..please notice only alogged in user can post the video)
		caption 		= "Here is some string as a video caption",
		audio_info	 	= "Diary of Jane by Breaking Benjamin"
	```

* **Response:**
	* Success:
	```javascript
		{
		  "data": {
		    "posterid": "1",
		    "posterusername": "test_username",
		    "upload_completed_time": "2020-02-11 18:25:57.653823",
		    "upload_started_time": "2020-02-11 18:25:57.173500",
		    "videofilename": "20200211182557dogvideo",
		    "videoid": "1"
		  },
		  "message": "Success"
		}
	```
	* Error:

		When Request header doesnot contain "multipart/form-data":
		```javascript
			{
				"message": "Invalid Request Header",
			  	"data": ""
			}
		```
		When the userid,caption,audio_info and givenvideosizeinkb are missing:
		```javascript
			{
			  "data": "",
			  "message": "Invalid Data Format"
			}
		```
		When the videofile is too large:
		** Please apply Video Compression (less than 150 MegaBytes)from the app-side so that there is no need to transfer that a big file through transfer Protocols via Internet ** 
		```javascript
			{
			  "data": "",
			  "message": "Filesize limit exceeded"
			}
		```
		When the userid doesnot exist or is not logged in yet:
		```javascript
			{
			  "data": "",
			  "message": "Invalid User Request"
			}
		```


### 2.b Newsfeed VideoPost
* **Type:** POST
* **Url:** 18.221.137.201:8080/api/newsfeed-videoposts
* **Request Header:**
	 contentType: 'application/json'
* **Request Body:**
	```javascript
	{
	 "api_secret_key":"c6fd54b7f4ad40ff9f1f75ab1ac77b10",
	 "userid":2,
	 "lastvideoid":-1       <==== NOTE
	 Suppose there are 20 videos in the database:
	 If "lastvideoid":-1 is given, latest ten videoposts(i.e from videoid 20 , 19,...to ...11) will be returned.
	 If you want older videoposts, then you can return foreg: lastvideoid=11 then videoposts(i.e from videoid 10 , 9,...to ...1) will be returned.
	}
	```


* **Response:**
	* Success:
	```javascript
	{
		"data": [
			{
				"audio_info": "Audio info",
				"caption": "hjvjvvi",
				"jsonurl": "18.221.137.201:8080/static/analyticsFolder/generated/static.json",
				"poster_email": "desktop1@domain.com",
				"poster_id": 2,
				"videoid": 26,
				"videourl": "18.221.137.201:8080/static/video/uploaded/202004161652351583427463073.mp4"
			},
			{
				"audio_info": "Audio info",
				"caption": "",
				"jsonurl": "18.221.137.201:8080/static/analyticsFolder/generated/static.json",
				"poster_email": "desktop1@domain.com",
				"poster_id": 2,
				"videoid": 25,
				"videourl": "18.221.137.201:8080/static/video/uploaded/202004161642511583427463073.mp4"
			},
			.
			.
			.
			.
			{
				"audio_info": "Audio info",
				"caption": "Video Caption",
				"jsonurl": "18.221.137.201:8080/static/analyticsFolder/generated/static.json",
				"poster_email": "desktop1@domain.com",
				"poster_id": 2,
				"videoid": 17,
				"videourl": "18.221.137.201:8080/static/video/uploaded/202003211520361583427463073.mp4"
			}
		],
		"message": "Success"
	}
	```
	* Error:

		When api key is invalid:
		```javascript
			{
			  "data": "",
			  "message": "Unauthenticated Request"
			}
		```

		When api key field is left empty:
		```javascript
			{
			  "data": "",
			  "message": "API Key Parsing Error"
			}
		```

		When the userid doesnot exist or is not logged in yet:
		```javascript
			{
			  "data": "",
			  "message": "Invalid User Request"
			}
		```

		When lastvideoid is empty:
		```javascript
			{
			  "data": "",
			  "message": "Invalid Data Format"
			}
		```
