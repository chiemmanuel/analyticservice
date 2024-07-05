import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/microservice_db') # Default URI if not specified
    DEFAULT_EMAIL = os.getenv('EMAIL', 'junor.chi-emmanuel-ngu@epita.fr') # Default email if not specified
    PORT = int(os.getenv('PORT', 5000))  # Default port is 5000 if not specified
    
