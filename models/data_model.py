from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import Flask

mongo = PyMongo()

class DataModel:
    @staticmethod
    def init_app(app: Flask):
        mongo.init_app(app)
        if "data" not in mongo.db.list_collection_names():
            mongo.db.create_collection("data")
    @staticmethod
    def save_data(data):
        return mongo.db.data.insert_one(data).inserted_id

    @staticmethod
    def get_data(data_id):
        return mongo.db.data.find_one({"_id": ObjectId(data_id)})
