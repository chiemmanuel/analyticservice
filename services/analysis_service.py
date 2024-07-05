import pandas as pd
from models.analysis_model import AnalysisModel
from models.data_model import DataModel

def analyze_data(data_id):
    data_record = DataModel.get_data(data_id)
    if not data_record:
        return None
    data_values = [row['values'] for row in data_record['data']]
    df = pd.DataFrame(data_values)

    df.columns = [f"col_{i}" for i in range(len(df.columns))]
    
    analysis_result = {
        "summary": {
            "mean": df.mean().to_dict(),
            "median": df.median().to_dict(),
            "std_dev": df.std().to_dict(),
            "correlation": df.corr().to_dict(),
            "covariance": df.cov().to_dict(),
            "variance": df.var().to_dict(),
            "skewness": df.skew().to_dict(),
            "kurtosis": df.kurt().to_dict()
        },
        "data_id": data_id
    }
    
    analysis_id = AnalysisModel.save_analysis(analysis_result)
    return analysis_id

def get_analysis_by_id(analysis_id):
    return AnalysisModel.get_analysis(analysis_id)
