import certifi
from motor.motor_asyncio import AsyncIOMotorClient
from mongoengine import connect
 
# MongoDB connection setup for motor
client = AsyncIOMotorClient(
    'mongodb+srv://myAtlasDBUser:Sai123@myatlasclusteredu.qifwasp.mongodb.net/taskmanagement?retryWrites=true&w=majority',
    tlsCAfile=certifi.where()
)
 
# Explicitly set the connection for mongoengine 
connect(
    db="taskmanagement",  # Name of the database
    host='mongodb+srv://myAtlasDBUser:Sai123@myatlasclusteredu.qifwasp.mongodb.net/taskmanagement?retryWrites=true&w=majority',
    alias='default'  # Default alias that mongoengine will use
)

#mongodb+srv://pradeep610:<db_password>@cluster0.v1vk1.mongodb.net/