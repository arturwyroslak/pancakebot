import requests
from src.config import PANCAKESWAP_API_URL

class PancakeSwapAPI:
    def __init__(self):
        self.api_url = PANCAKESWAP_API_URL

    def get_market_data(self):
        """
        Fetches real-time market data from PancakeSwap API.
        """
        try:
            response = requests.get(f"{self.api_url}/market-data")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")

    def get_liquidity_data(self):
        """
        Fetches liquidity data from PancakeSwap API.
        """
        try:
            response = requests.get(f"{self.api_url}/liquidity-data")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")

    def get_transaction_volume(self):
        """
        Fetches transaction volume data from PancakeSwap API.
        """
        try:
            response = requests.get(f"{self.api_url}/transaction-volume")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")

    import unittest
    from unittest.mock import patch
    class TestPancakeSwapAPI(unittest.TestCase):
        def setUp(self):
            self.api = PancakeSwapAPI()
        def test_get_market_data_success(self):
            with patch('requests.get') as mocked_get:
                mocked_get.return_value.status_code = 200
                mocked_get.return_value.json.return_value = {'data': 'market data'}
                data = self.api.get_market_data()
                self.assertEqual(data, {'data': 'market data'})
        def test_get_market_data_failure(self):
            with patch('requests.get') as mocked_get:
                mocked_get.return_value.status_code = 404
                mocked_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()
                data = self.api.get_market_data()
                self.assertIsNone(data)
        def test_get_liquidity_data_success(self):
            with patch('requests.get') as mocked_get:
                mocked_get.return_value.status_code = 200
                mocked_get.return_value.json.return_value = {'data': 'liquidity data'}
                data = self.api.get_liquidity_data()
                self.assertEqual(data, {'data': 'liquidity data'})
        def test_get_liquidity_data_failure(self):
            with patch('requests.get') as mocked_get:
                mocked_get.return_value.status_code = 500
                mocked_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()
                data = self.api.get_liquidity_data()
                self.assertIsNone(data)
    if __name__ == '__main__':
        unittest.main()