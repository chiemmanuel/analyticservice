from flask import Flask, render_template
from flask_restful import Api
from routes.data_routes import DataFetchResource
from routes.analysis_routes import DataAnalysisResource, AnalysisDetailResource
from services.visualization_service import generate_visualization
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

@app.route('/visualize/<analysis_id>', methods=['GET'])
def visualize_analysis(analysis_id):
    analysis_details = generate_visualization(analysis_id)
    if not analysis_details:
        return "analysis not available", 404
    return render_template('visualization.html', **analysis_details)

if __name__ == '__main__':
    app.run(port=app.config['PORT'])
