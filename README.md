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

### Create User
* **Type:** POST
* **Url:** 18.221.137.201:8080/api/create-user
* **Request Header:**
	 contentType: 'application/json'
* **Request Body:**
	{
		"api_secrect_key":"your valid secret key",
		"gender":"male/female/other"
		"username":"username",
		"firstname":"firstname",
		"lastname":"lastname",
		"dateofbirth":"DateTime data",
		"phonenumber":"9876543210",
		"email":"user@domain.com"
	}

* **Response:**
	* Success:
		{
			"message":"Success",<br>
			"data":[<br>
				"userid":"32",<br>
				"gender":"male/female/other",<br>
				"username":"username",<br>
				"firstname":"firstname",<br>
				"lastname":"lastname",<br>
				"dateofbirth":"DateTimedata",<br>
				"created_datetime":"createdTimedata"<br>
				"phonenumber":"9876543210",<br>
				"email":"user@domain.com"<br>
			]<br>
		}<br>
	* Error:
		When Request header is other than "application/json":
			{<br>
				"message": "Invalid Request Header",<br>
			  	"data": "" <br>
			}<br>
		When api_secrect_key is invalid:
			{<br>
				"message": "Unauthenticated Request",<br>
				"data": ""<br>
			}<br>
		When dataofbirth,phonenumber or email are invalid:
			{<br>
				"message": "Invalid Data Format",<br>
				"data": ""<br>
			}<br>