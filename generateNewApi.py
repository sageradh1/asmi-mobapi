import uuid
from app.database.models import APIAuthKey
from app import db
from datetime import datetime,timedelta

print(str(uuid.uuid4()))
API_Key=uuid.uuid4().hex
print(API_Key)
api_generatedTime = datetime.utcnow()
api_expiry_date = api_generatedTime +timedelta(days=3650)
print(api_generatedTime)
print(api_expiry_date)

try:
	newKey = APIAuthKey(api_key=API_Key, generate_date=api_generatedTime,expiry_date=api_expiry_date)
	db.session.add(newKey)
	db.session.commit()
except Exception as err:
	#print(type(inst))    # the exception instance
	#print(inst.args)     # arguments stored in .args
	print(inst)