
import unittest
from unittest.mock import patch
from src import pancakeswap_api

class TestPancakeSwapAPI(unittest.TestCase):

    @patch('src.pancakeswap_api.requests.get')
    def test_get_market_data(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {
            'liquidity': 1000000,
            'price': 0.01,
            'volume': 500000
        }

        data = pancakeswap_api.get_market_data()
        self.assertEqual(data, {'liquidity': 1000000, 'price': 0.01, 'volume': 500000})
        mock_get.assert_called_once_with(pancakeswap_api.API_URL)
        # Test for HTTPError
        mock_get.side_effect = HTTPError()
        with self.assertRaises(pancakeswap_api.MarketDataHTTPError):
            pancakeswap_api.get_market_data()
        mock_get.assert_called_with(pancakeswap_api.API_URL)
        # Test for RequestException
        mock_get.side_effect = RequestException()
        with self.assertRaises(pancakeswap_api.MarketDataRequestError):
            pancakeswap_api.get_market_data()
        mock_get.assert_called_with(pancakeswap_api.API_URL)
    @patch('src.pancakeswap_api.requests.get')
    def test_get_price_data(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {
            'BNB': 400,
            'CAKE': 20,
            'BUSD': 1
        }

        data = pancakeswap_api.get_price_data()
        self.assertEqual(data, {'BNB': 400, 'CAKE': 20, 'BUSD': 1})
        mock_get.assert_called_once_with(pancakeswap_api.ORACLE_URL)

if __name__ == '__main__':
    unittest.main()
