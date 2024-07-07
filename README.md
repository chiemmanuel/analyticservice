# analyticservice
This project is a microservice that allows users to fetch data using a call to another microservice, analyze this data and visualize it.
The API provides endpoints to fetch, analyze and visualize data.

This service is intended to be used in conjunction with the [excel service](https://github.com/Travis-Berthrong/excelservice) (Travis Berthrong) which uses the data in the excel workbook to perform data analysis and visualization. A core service (Ilia Tiskin) is used to provide a common public-facing interface for the two services

# Dependencies
pip install flask flask_pymongo flask_restful requests pandas matplotlib

# Run app
python app.py

The server will start at `http://127.0.0.1:5000` (or the port specified in the `.env` file).

## Usage

### API Endpoints

- **Fetch Data**: Fetch data from an external service and store it temporarily.
    ```http
    GET /analysisApi/fetch-data?sheetName=<sheetName>&tableName=<tableName>&email=<email>
    ```
    - **Parameters**: 
        - `sheetName` (query param): Name of the sheet to fetch data from.
        - `tableName` (query param): Name of the table to fetch data from.
        - `email` (query param): email to create graphApi session.

    - **Response**:
        - `200 OK`: Returns `data_id` which can be used for analysis.
        - `400 Bad Request`: If sheet name or table name is not provided.
        - `500 Internal Server Error`: If fetching or storing data fails.

- **Analyze Data**: Perform analysis on the fetched data.
    ```http
    POST /analysisApi/analyze?dataId=<dataId>
    ```
    - **Parameters**: 
        - `dataId` (query param): ID of the data to be analyzed.
    - **Response**:
        - `201 Created`: Returns `analysis_id` which can be used for visualization.
        - `400 Bad Request`: If data ID is not provided.
        - `500 Internal Server Error`: If analysis fails.

- **Get Analysis Details**: Retrieve analysis details by analysis ID.
    ```http
    GET /analysisApi/analysis/<analysis_id>
    ```
    - **Parameters**: 
        - `analysis_id` (path param): ID of the analysis to be retrieved.
    - **Response**:
        - `200 OK`: Returns the analysis details.
        - `404 Not Found`: If analysis is not found.

- **Visualize Data**: Generate and display visualizations for the analysis.
    ```http
    GET /analysisApi/visualize/<analysis_id>
    ```
    - **Parameters**: 
        - `analysis_id` (path param): ID of the analysis to be visualized.
    - **Response**:
        - `200 OK`: Returns the rendered HTML with visualizations.
        - `404 Not Found`: If visualization is not available.