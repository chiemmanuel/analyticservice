from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = PyMongo()

class AnalysisModel:
    @staticmethod
    def save_analysis(data):
        return mongo.db.analyses.insert_one(data).inserted_id

    @staticmethod
    def get_analysis(analysis_id):
        return mongo.db.analyses.find_one({"_id": ObjectId(analysis_id)})
