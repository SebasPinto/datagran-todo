from mongoengine import *

connect('TodoList')

class User(Document):
	email = EmailField(required=True, unique=True)
	password = StringField(required=True, max_length=32)

class Task(Document):
	status = IntField(required=True)
	description = StringField(required=True)
	user = EmailField(required=True)