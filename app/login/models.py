import os, sys
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from passlib.apps import custom_app_context as pwd_context

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:b3nder1sgr8@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class UserModel(db.Model):
	__tablename__='user'
	__table_args__={'schema':'share'}
	id = db.Column('user_id', db.Integer, autoincrement=True, primary_key=True)
	username = db.Column('username', db.String(64), unique = True, index = True)
	password = db.Column('password', db.String(256))
	email = db.Column('email', db.String(64))
	create_dt = db.Column('create_dt', db.DateTime)

	def __init__(self, username, password, email):
		self.username = username
		self.password = self.set_password(password)
		self.email = email
		self.create_dt = datetime.datetime.utcnow()

	def set_password(self, password):
		return pwd_context.hash(password)

	def __repr__(self):
		return '<id {}>'.format(self.id)


db.create_all()
