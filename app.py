from flask import Flask
from flask_restful import Api
from routes.data_routes import DataFetchResource
from routes.analysis_routes import DataAnalysisResource, AnalysisDetailResource
from routes.visualization_routes import VisualizationResource
from config import Config
from models.data_model import DataModel
from models.analysis_model import AnalysisModel

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

DataModel.init_app(app)
AnalysisModel.init_app(app)

api.add_resource(DataFetchResource, '/fetch-data')
api.add_resource(DataAnalysisResource, '/analyze')
api.add_resource(AnalysisDetailResource, '/analysis/<analysis_id>')
api.add_resource(VisualizationResource, '/visualize/<analysis_id>')

if __name__ == '__main__':
    app.run(port=app.config['PORT'])
