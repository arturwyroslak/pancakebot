import requests

import unittest
from unittest.mock import patch
from src.config import ORACLE_API_URLS

class Oracle:
    def __init__(self):
        self.oracles = ORACLE_API_URLS

    def get_price_data(self, token):
        price_data = {}
        for oracle_name, oracle_url in self.oracles.items():
            try:
                response = requests.get(oracle_url.format(token))
                response.raise_for_status()
                price_data[oracle_name] = response.json()['price']
            except requests.exceptions.RequestException as err:
                print(f"Error fetching price data from {oracle_name}: {err}")
        return price_data
class TestOracle(unittest.TestCase):
    def setUp(self):
        self.oracle = Oracle()
    
    def test_get_price_data_success(self):
        token = "TEST_TOKEN"
        mock_response = {'price': 100}
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.json.return_value = mock_response
            price_data = self.oracle.get_price_data(token)
            self.assertIn('oracle_name', price_data)
            self.assertEqual(price_data['oracle_name'], mock_response['price'])
    
    def test_get_price_data_request_exception(self):
        token = "TEST_TOKEN"
        with patch('requests.get') as mocked_get:
            mocked_get.side_effect = requests.exceptions.RequestException("An error occurred")
            price_data = self.oracle.get_price_data(token)
            self.assertEqual(price_data, {})

if __name__ == '__main__':
    unittest.main()
