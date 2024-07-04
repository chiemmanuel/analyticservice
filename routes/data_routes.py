from flask_restful import Resource
from flask import request
from services.data_service import fetch_and_store_data

class DataFetchResource(Resource):
    def get(self):
        sheet_name = request.args.get('sheetName')
        table_name = request.args.get('tableName')
        
        if not sheet_name or not table_name:
            return {"message": "Invalid sheet name or table name"}, 400
        
        data_id = fetch_and_store_data(sheet_name, table_name)
        
        if not data_id:
            return {"message": "Failed to fetch or store data"}, 500
        
        return {"data_id": str(data_id)}, 200
