import requests
from models.data_model import DataModel

def fetch_and_store_data(sheet_name, table_name):
    try:
        url = f"http://localhost:8001/excel_sheets/table/{table_name}?{sheet_name}"
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        data_id = DataModel.save_data({"sheet_name": sheet_name, "table_name": table_name, "data": data})
        return data_id
    except requests.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return None
