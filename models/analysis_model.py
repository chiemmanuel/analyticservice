from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = PyMongo()

class AnalysisModel:
    @staticmethod
    def init_app(app):
        mongo.init_app(app)
        if "analyses" not in mongo.db.list_collection_names():
            mongo.db.create_collection("analyses")

    @staticmethod
    def save_analysis(data):
        return mongo.db.analyses.insert_one(data).inserted_id

    @staticmethod
    def get_analysis(analysis_id):
        analysis = mongo.db.analyses.find_one({"_id": ObjectId(analysis_id)})
        analysis["_id"] = str(analysis["_id"])
        return analysis
