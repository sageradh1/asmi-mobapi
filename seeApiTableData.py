from app.database.models import APIAuthKey

def seeFunction():
	try:
		##To load all the data
		apiauthkeys = APIAuthKey.query.all()
		##To load according to specific id
		# id=1
		# apiauthkeys= APIAuthKey.query.get(id)

		if apiauthkeys is None:
			print("None type detected")
			return

		for apiauthkey in apiauthkeys:
			print(apiauthkey.id,apiauthkey.api_key)
	except Exception as ex:
		print(type(ex))
		
seeFunction()