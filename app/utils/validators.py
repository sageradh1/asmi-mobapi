import re

def isValidPhoneNumber(phone_number):
	if len(phone_number) != 10:
		return False
	if not phone_number.isdecimal():
		return False
	if phone_number[0]!="9":
		return False
	return True

def isValidEmail(email_address):
	regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
	if(re.search(regex,email_address)):  
		return True  
	else:  
		return False