from mongoengine import *
import datetime

class UserCreate(Document):
    userName=StringField()
    userEmail=StringField()
    password=StringField()
    type=StringField()

class Task(Document):
    taskName = StringField()
    tasktitle =StringField()
    taskDescription = StringField()