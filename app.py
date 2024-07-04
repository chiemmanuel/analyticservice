from flask import Flask
from flask_restful import Api
from routes.data_routes import DataFetchResource
from routes.analysis_routes import DataAnalysisResource, AnalysisDetailResource
from routes.visualization_routes import VisualizationResource
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

api.add_resource(DataFetchResource, '/analysisApi/fetch-data')
api.add_resource(DataAnalysisResource, '/analysisApi/analyze')
api.add_resource(AnalysisDetailResource, '/analysisApi/analysis/<analysis_id>')
api.add_resource(VisualizationResource, '/analysisApi/visualize/<analysis_id>')

if __name__ == '__main__':
    app.run(port=app.config['PORT'])
