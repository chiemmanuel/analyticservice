import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/microservice_db')
    PORT = int(os.getenv('PORT', 5000))  # Default port is 5000 if not specified
