# ASMI API
## Version 1.0.0

###### The latest requirements are included in :requirements2DInjectionMerge.txt

###### Extra dependencies that are installed out of virtual env
(or out of requirements2DInjectionMerge.txt):
- Postgresql
- Python 3.6.9


###### Note These requirements are not be ignored:
- Tensorflow version 1.13.2 or 1.14.0

## API Documentation

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



### Create User
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


### User Login
* **Type:** GET
* **Url:** 18.221.137.201:8080/api/user-login
* **Request Header:**
	 contentType: 'application/json'
* **Request Body:**
	```javascript
		{
			"api_secrect_key":"your valid secret key",
			"username":"username",
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

### User Logout
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

