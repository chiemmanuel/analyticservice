from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = PyMongo()

class DataModel:
    @staticmethod
    def save_data(data):
        return mongo.db.data.insert_one(data).inserted_id

    @staticmethod
    def get_data(data_id):
        return mongo.db.data.find_one({"_id": ObjectId(data_id)})
