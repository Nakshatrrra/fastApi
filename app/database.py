import motor.motor_asyncio
from decouple import config

# MongoDB connection URI
MONGO_DETAILS = config("MONGO_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client['fastapi_database']

# Define collection
user_collection = database.get_collection('users')
