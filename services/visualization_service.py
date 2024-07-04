from models.analysis_model import AnalysisModel
from models.data_model import DataModel
import base64
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt

def generate_visualization(analysis_id):
    # Get analysis result based on analysis_id
    analysis_result = AnalysisModel.get_analysis(analysis_id)
    if not analysis_result:
        return None

    try:
        # Extract summary and data_id from analysis_result
        summary = analysis_result.get('summary', {})
        data_id = analysis_result.get('data_id')
        
        # Fetch raw data for more complex visualizations if needed
        raw_data = DataModel.get_data(data_id)
        df = pd.DataFrame.from_dict(raw_data['data'])
        
        # Create subplots for visualizations
        fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 15))
        
        # Plotting raw data overview
        df.plot(ax=axes[0, 0], title="Data Overview")
        
        # Plotting summary statistics
        pd.Series(summary.get('mean', {})).plot(kind='bar', ax=axes[0, 1], title="Mean Values")
        pd.Series(summary.get('median', {})).plot(kind='bar', ax=axes[1, 0], title="Median Values")
        pd.Series(summary.get('std_dev', {})).plot(kind='bar', ax=axes[1, 1], title="Standard Deviation")
        pd.Series(summary.get('skewness', {})).plot(kind='bar', ax=axes[2, 0], title="Skewness")
        pd.Series(summary.get('kurtosis', {})).plot(kind='bar', ax=axes[2, 1], title="Kurtosis")
        
        # Correlation and covariance matrix plots (if required)
        # These can be added as additional plots if needed.
        
        # Save the plot as an image
        img = BytesIO()
        plt.tight_layout()
        plt.savefig(img, format='png')
        img.seek(0)
        
        # Convert the image to base64 string
        img_base64 = base64.b64encode(img.getvalue()).decode('utf8')

        return {
            'visualization': img_base64,
            'summary': summary
        }
    except Exception as error:
        # Print error message if an exception occurs
        print(f"Error during visualization: {error}")
        return None
