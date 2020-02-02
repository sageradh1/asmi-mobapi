from app import db
from datetime import datetime
from sqlalchemy_utils import PhoneNumber


#Migration title should be "Added Auth table, Added isActive and lastonlinetime"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(64), index=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))    
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True,unique=True)
    _phone_number = db.Column(db.Unicode(255))
    phone_country_code = db.Column(db.Unicode(8))

    phone_number = db.composite(
        PhoneNumber,
        _phone_number,
        phone_country_code
    )
    date_of_birth = db.Column(db.DateTime, index=True, nullable=False)
    created_datetime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    password_hash = db.Column(db.String(128))
    video_posts = db.relationship('VideoPost', backref='author', lazy='dynamic')
    is_active = db.Column(db.Boolean, unique=False, default=True)
    lastonline_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
    	return '<User {}>'.format(self.username)

class VideoPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), unique=True)
    extension = db.Column(db.String(5))
    storagelocation = db.Column(db.String(500))
    upload_started_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    upload_completed_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)    
    last_modified_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    caption = db.Column(db.String(440))
    audio_info=db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<VideoPost id:{} Uploaded by:{} at {}>'.format(self.id,self.user_id,self.upload_completed_time)

class APIAuthKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.String(100))
    generate_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    expiry_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)