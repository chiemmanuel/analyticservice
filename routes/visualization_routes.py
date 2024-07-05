from flask import render_template
from flask_restful import Resource
from services.visualization_service import generate_visualization

class VisualizationResource(Resource):
    def get(self, analysis_id):
        if not analysis_id:
            return {"message": "Analysis ID is required"}, 400
        analysis_details = generate_visualization(analysis_id)
        if not analysis_details:
            return {"message": "Visualization not available"}, 404
        return render_template('visualization.html', **analysis_details)
