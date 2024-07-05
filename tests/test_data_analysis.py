import unittest
from unittest.mock import patch
from app import app

class TestDataAnalysisResource(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('services.analysis_service.analyze_data')
    def test_analyze_data_success(self, mock_analyze_data):
        mock_analyze_data.return_value = 'analysis_id'

        response = self.app.post('/analyze?dataId=data_id')
        self.assertEqual(response.status_code, 201)
        self.assertIn('analysis_id', response.json)

    @patch('services.analysis_service.analyze_data')
    def test_analyze_data_failure(self, mock_analyze_data):
        mock_analyze_data.return_value = None

        response = self.app.post('/analyze?dataId=data_id')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json['message'], 'Analysis failed')

if __name__ == '__main__':
    unittest.main()
