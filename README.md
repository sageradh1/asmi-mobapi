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
Type:POST
Url: 18.221.137.201:8080/api/create-user
Request Header:
	 contentType: 'application/json'
Request Body:
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

Response:
	Success:
		{
			"message":"Success",
			"data":[
				"userid":"32",
				"gender":"male/female/other",
				"username":"username",
				"firstname":"firstname",
				"lastname":"lastname",
				"dateofbirth":"DateTimedata",
				"created_datetime":"createdTimedata"
				"phonenumber":"9876543210",
				"email":"user@domain.com"
			]
		}
	Error:
		When Request header is other than "application/json":
			{
				"message": "Invalid Request Header",
			  	"data": "" 
			}
		When api_secrect_key is invalid:
			{
				"message": "Unauthenticated Request",
				"data": ""
			}
		When dataofbirth,phonenumber or email are invalid:
			{
				"message": "Invalid Data Format",
				"data": ""
			}