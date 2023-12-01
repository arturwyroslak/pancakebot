```python
import unittest
from unittest.mock import patch
from src import portfolio_balancing

class TestPortfolioBalancing(unittest.TestCase):

    @patch('src.portfolio_balancing.get_market_data')
    @patch('src.portfolio_balancing.get_price_data')
    @patch('src.portfolio_balancing.balance_portfolio')
    def test_balance_portfolio(self, mock_balance_portfolio, mock_get_price_data, mock_get_market_data):
        mock_get_market_data.return_value = {'BNB': {'price': 500, 'volume': 10000}, 'CAKE': {'price': 20, 'volume': 5000}}
        mock_get_price_data.return_value = {'BNB': 500, 'CAKE': 20}
        mock_balance_portfolio.return_value = {'BNB': 0.6, 'CAKE': 0.4}

        result = portfolio_balancing.balance_portfolio()

        self.assertEqual(result, {'BNB': 0.6, 'CAKE': 0.4})
        mock_get_market_data.assert_called_once()
        mock_get_price_data.assert_called_once()
        mock_balance_portfolio.assert_called_once()

    @patch('src.portfolio_balancing.get_market_data')
    @patch('src.portfolio_balancing.get_price_data')
    @patch('src.portfolio_balancing.balance_portfolio')
    def test_balance_portfolio_market_change(self, mock_balance_portfolio, mock_get_price_data, mock_get_market_data):
        mock_get_market_data.return_value = {'BNB': {'price': 600, 'volume': 12000}, 'CAKE': {'price': 15, 'volume': 4000}}
        mock_get_price_data.return_value = {'BNB': 600, 'CAKE': 15}
        mock_balance_portfolio.return_value = {'BNB': 0.7, 'CAKE': 0.3}

        result = portfolio_balancing.balance_portfolio()

        self.assertEqual(result, {'BNB': 0.7, 'CAKE': 0.3})
        mock_get_market_data.assert_called_once()
        mock_get_price_data.assert_called_once()
        mock_balance_portfolio.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```