import pandas as pd
from src.pancakeswap_api import get_market_data
from src.oracles import get_price_data
from src.trading_strategies import apply_trading_strategy
from src.config import load_config

class PortfolioBalancer:
    def __init__(self):
        self.config = load_config()
        self.assets = self.config['assets']
        self.portfolio = pd.DataFrame(columns=['asset', 'quantity', 'value'])

    def balance_portfolio(self):
        market_data = get_market_data()
        price_data = get_price_data()

        for asset in self.assets:
            asset_data = market_data[market_data['asset'] == asset]
            asset_price = price_data[price_data['asset'] == asset]['price']
            asset_quantity = self.portfolio[self.portfolio['asset'] == asset]['quantity']

            if not asset_data.empty and not asset_price.empty:
                asset_value = asset_quantity * asset_price
                self.portfolio.loc[self.portfolio['asset'] == asset, 'value'] = asset_value

        total_value = self.portfolio['value'].sum()
        self.portfolio['weight'] = self.portfolio['value'] / total_value

        target_weights = apply_trading_strategy(self.portfolio, market_data)

        rebalance_orders = self._get_rebalance_orders(target_weights)

        return rebalance_orders

    def _get_rebalance_orders(self, target_weights):
        rebalance_orders = []

        for index, row in self.portfolio.iterrows():
            asset = row['asset']
            current_weight = row['weight']
            target_weight = target_weights[asset]

            if current_weight < target_weight:
                rebalance_orders.append({
                    'action': 'BUY',
                    'asset': asset,
                    'quantity': (target_weight - current_weight) * self.portfolio['value'].sum()
                })
            elif current_weight > target_weight:
                rebalance_orders.append({
                    'action': 'SELL',
                    'asset': asset,
                    'quantity': (current_weight - target_weight) * self.portfolio['value'].sum()
                })

        return rebalance_orders

import unittest
from unittest.mock import MagicMock

class TestPortfolioBalancer(unittest.TestCase):

    def setUp(self):
        # Mock the load_config and external data fetching functions
        with unittest.mock.patch('src.config.load_config', return_value={'assets': ['BTC', 'ETH']}):
            from src.pancakeswap_api import get_market_data
            from src.oracles import get_price_data
            from src.trading_strategies import apply_trading_strategy

            # Mocking the market and price data with example values for testing
            get_market_data_mock = MagicMock(return_value=pd.DataFrame({
                'asset': ['BTC', 'ETH'],
                'market_value': [50000, 2500]
            }))
            get_price_data_mock = MagicMock(return_value=pd.DataFrame({
                'asset': ['BTC', 'ETH'],
                'price': [51000, 2400]
            }))
            apply_trading_strategy_mock = MagicMock(return_value={'BTC': 0.6, 'ETH': 0.4})

            # Create a test instance of the PortfolioBalancer
            self.portfolio_balancer = PortfolioBalancer()
            self.portfolio_balancer.portfolio = pd.DataFrame({
                'asset': ['BTC', 'ETH'],
                'quantity': [1, 10],
                'value': [50000, 25000]
            })
            self.portfolio_balancer.assets = ['BTC', 'ETH']

    def test_balance_portfolio(self):
        # Run the balance_portfolio method to update weights
        self.portfolio_balancer.balance_portfolio()

        # Check the portfolio values have been updated correctly
        expected_portfolio_values = pd.DataFrame({
            'asset': ['BTC', 'ETH'],
            'quantity': [1, 10],
            'value': [51000, 24000],
            'weight': [0.6800, 0.3200]  # Calculated based on the mock price data provided
        })
        pd.testing.assert_frame_equal(self.portfolio_balancer.portfolio, expected_portfolio_values, check_dtype=False)

    def test_get_rebalance_orders(self):
        # Pre-calculate the weight and get the rebalance orders
        self.portfolio_balancer.balance_portfolio()
        rebalance_orders = self.portfolio_balancer._get_rebalance_orders({'BTC': 0.5, 'ETH': 0.5})

        # Check if the generated rebalance orders match the expected orders
        expected_rebalance_orders = [
            {'action': 'SELL', 'asset': 'BTC', 'quantity': 90.00},
            {'action': 'BUY',  'asset': 'ETH', 'quantity': 60.00}
        ]  # Assuming total value = 75000, BTC weight to reduce by 0.18, ETH weight to increase by 0.18

        self.assertEqual(rebalance_orders, expected_rebalance_orders)

if __name__ == '__main__':
    unittest.main()
