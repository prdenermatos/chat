from src.app import db
import datetime

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50))
   messages = db.relationship('Message', backref='user', lazy=True)

class Message(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   content = db.Column(db.String(500))
   timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.now())
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
