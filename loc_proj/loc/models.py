from datetime import datetime
import pytz
from loc import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    locations=db.relationship('Post', backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email},'{self.image_file}')"

now = datetime.now()
tz = pytz.timezone('Asia/Kolkata')
your_now = now.astimezone(tz)

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    loc=db.Column(db.String(60),nullable=False)
    date=db.Column(db.DateTime,nullable=False,default=your_now)
    message=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"User('{self.loc}','{self.date},'{self.message}')"