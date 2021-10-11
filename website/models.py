from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class TestPC(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	ip_address = db.Column(db.String(15))
	status = db.Column(db.String(30))

class Platform(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	ip_address = db.Column(db.String(15))
	status = db.Column(db.String(30))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(15))
	password = db.Column(db.String(20))