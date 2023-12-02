import unittest
from unittest.mock import patch

from src.yield_farming import YieldFarmingManager


class TestYieldFarmingManager(unittest.TestCase):
    def setUp(self):
        self.manager = YieldFarmingManager()

    @patch('src.yield_farming.get_market_data')
    @patch('src.yield_farming.get_price_data')
    def test_manage_yield_farming(self, mock_get_price_data, mock_get_market_data):
        mock_get_market_data.return_value = {'pool1': {'apy': 15, 'target_price': 1.05}}
        mock_get_price_data.return_value = {'pool1': 1.1}
        self.manager.manage_yield_farming()
        self.assertTrue(self.manager.should_add_liquidity.called)

    def test_should_add_liquidity(self):
        pool_data = {'apy': 15, 'target_price': 1.05}
        pool_price = 1.1
        self.assertTrue(self.manager.should_add_liquidity(pool_data, pool_price))

    def test_should_remove_liquidity(self):
        pool_data = {'apy': 15, 'target_price': 1.05}
        pool_price = 0.9
        self.assertTrue(self.manager.should_remove_liquidity(pool_data, pool_price))

    @patch('src.yield_farming.execute_transaction')
    def test_add_liquidity(self, mock_execute_transaction):
        pool = {'tokenA': '0x...', 'tokenB': '0x...', 'amountA': 1, 'amountB': 1, 'slippage': 0.01, 'deadline': 1622540400}
        self.manager.add_liquidity(pool)
        self.assertTrue(mock_execute_transaction.called)

    @patch('src.yield_farming.execute_transaction')
    def test_remove_liquidity(self, mock_execute_transaction):
        pool = {'liquidity': 1, 'amountAMin': 0.9, 'amountBMin': 0.9, 'deadline': 1622540400}
        self.manager.remove_liquidity(pool)
        self.assertTrue(mock_execute_transaction.called)

    def test_analyze_impermanent_loss(self):
        original_price_ratio = 1
        current_price_ratio = 1.1
        expected_impermanent_loss = 0.04880884817015167
        self.assertAlmostEqual(self.manager.analyze_impermanent_loss(original_price_ratio, current_price_ratio), expected_impermanent_loss)

if __name__ == '__main__':
    unittest.main()
