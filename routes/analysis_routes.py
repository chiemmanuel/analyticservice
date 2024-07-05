from flask_restful import Resource
from services.analysis_service import analyze_data, get_analysis_by_id
from flask import request
from bson import ObjectId

class DataAnalysisResource(Resource):
    def post(self):
        data_id = request.args.get('dataId')
        if not data_id or not ObjectId.is_valid(data_id):
            return {"message": "Invalid data ID"}, 400
        
        analysis_id = analyze_data(data_id)
        if not analysis_id:
            return {"message": "Analysis failed"}, 500
        return {"analysis_id": str(analysis_id)}, 201

class AnalysisDetailResource(Resource):
    def get(self, analysis_id):
        analysis = get_analysis_by_id(analysis_id)
        if not analysis:
            return {"message": "Analysis not found"}, 404
        return analysis, 200
