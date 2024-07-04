from models.analysis_model import AnalysisModel
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import pandas as pd

def generate_visualization(analysis_id):
    analysis_result = AnalysisModel.get_analysis(analysis_id)
    if not analysis_result:
        return None

    try:
        df = pd.DataFrame.from_dict(analysis_result['data'])
        
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
        df.plot(ax=axes[0, 0], title="Data Overview")
        df.mean().plot(kind='bar', ax=axes[0, 1], title="Mean Values")
        df.median().plot(kind='bar', ax=axes[1, 0], title="Median Values")
        pd.plotting.scatter_matrix(df, ax=axes[1, 1])

        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        
        img_base64 = base64.b64encode(img.getvalue()).decode('utf8')
        return img_base64
    except Exception as error:
        print(f"Error during visualization: {error}")
        return None
