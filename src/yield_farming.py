import json

from src.config import load_config
from src.impermanent_loss import analyze_impermanent_loss
from src.oracles import get_price_data
from src.pancakeswap_api import get_market_data
from src.smart_contracts import execute_transaction
from web3 import Web3


class YieldFarmingManager:
    def __init__(self):
        self.config = load_config()
        self.web3 = Web3(Web3.HTTPProvider(self.config['blockchain_network']))
        self.pancake_swap_contract = self.web3.eth.contract(address=self.config['pancake_swap_contract_address'], abi=json.loads(self.config['pancake_swap_contract_abi']))

    def manage_yield_farming(self):
        market_data = get_market_data()
        price_data = get_price_data()

        for pool in self.config['pools']:
            pool_data = market_data[pool]
            pool_price = price_data[pool]

            if self.should_add_liquidity(pool_data, pool_price):
                self.add_liquidity(pool)
            elif self.should_remove_liquidity(pool_data, pool_price):
                self.remove_liquidity(pool)

    def should_add_liquidity(self, pool_data, pool_price):
        # Logic for when to add liquidity
        price_difference_threshold = 0.05 # e.g., 5%
        high_apy_threshold = 10 # e.g., 10%
        current_price_to_target_ratio = pool_price / pool_data['target_price']
        price_spread_significant = abs(1 - current_price_to_target_ratio) > price_difference_threshold
        apy_high = pool_data['apy'] > high_apy_threshold
        return price_spread_significant or apy_high

    def should_remove_liquidity(self, pool_data, pool_price):
        # Logic for when to remove liquidity
        impermanent_loss_threshold = 0.10 # e.g., 10%
        impermanent_loss = self.analyze_impermanent_loss(pool_data, pool_price)
        return impermanent_loss > impermanent_loss_threshold

    def add_liquidity(self, pool):
        # Extract token addresses, amounts, slipperage settings from the pool config
        tokenA = pool['tokenA']
        tokenB = pool['tokenB']
        amountA = pool['amountA']
        amountB = pool['amountB']
        slippage = pool['slippage']
        deadline = pool['deadline']
        # Convert them into parameters for PancakeSwap contract interaction
        parameters = [tokenA, tokenB, amountA, amountB, slippage, deadline]
        # Use the relevant functions from src/smart_contracts.py to build and execute the add liquidity transaction
        try:
            execute_transaction(self.pancake_swap_contract.functions.addLiquidityETH, parameters)
        except Exception as e:
            print(f"Failed to add liquidity due to: {str(e)}")

    def remove_liquidity(self, pool):
        # Extract liquidity, minimum amounts, and deadline from the pool config
        liquidity = pool['liquidity']
        amountAMin = pool['amountAMin']
        amountBMin = pool['amountBMin']
        deadline = pool['deadline']
        # Convert them into parameters for PancakeSwap contract interaction
        parameters = [liquidity, amountAMin, amountBMin, deadline]
        # Use the relevant functions from src/smart_contracts.py to build and execute the remove liquidity transaction
        try:
            execute_transaction(self.pancake_swap_contract.functions.removeLiquidityETH, parameters)
        except Exception as e:
            print(f"Failed to remove liquidity due to: {str(e)}")
import unittest
from unittest.mock import Mock, patch


class TestYieldFarmingManager(unittest.TestCase):
    def setUp(self):
        self.manager = YieldFarmingManager()
        self.pool = {
            'tokenA': '0x...',
            'tokenB': '0x...',
            'amountA': 1,
            'amountB': 1,
            'slippage': 0.01,
            'deadline': 1622540400
        }

    @patch('src.yield_farming.execute_transaction')
    def test_add_liquidity_success(self, mock_execute):
        mock_execute.return_value = True
        self.manager.add_liquidity(self.pool)
        mock_execute.assert_called_once()

    @patch('src.yield_farming.execute_transaction')
    def test_add_liquidity_failure(self, mock_execute):
        mock_execute.side_effect = Exception('Failed to add liquidity')
        self.manager.add_liquidity(self.pool)
        mock_execute.assert_called_once()

    @patch('src.yield_farming.execute_transaction')
    def test_remove_liquidity_success(self, mock_execute):
        mock_execute.return_value = True
        self.manager.remove_liquidity(self.pool)
        mock_execute.assert_called_once()

    @patch('src.yield_farming.execute_transaction')
    def test_remove_liquidity_failure(self, mock_execute):
        mock_execute.side_effect = Exception('Failed to remove liquidity')
        self.manager.remove_liquidity(self.pool)
        mock_execute.assert_called_once()

if __name__ == '__main__':
    unittest.main()
        # Extract liquidity, minimum amounts, and deadline from the pool config
        liquidity = pool['liquidity']
        amountAMin = pool['amountAMin']
        amountBMin = pool['amountBMin']
        deadline = pool['deadline']
        # Convert them into parameters for PancakeSwap contract interaction
        parameters = [liquidity, amountAMin, amountBMin, deadline]
        # Use the relevant functions from src/smart_contracts.py to build and execute the remove liquidity transaction
        execute_transaction(self.pancake_swap_contract.functions.removeLiquidityETH, parameters)

    def analyze_impermanent_loss(self, original_price_ratio, current_price_ratio):
        """
        Analyze potential impermanent loss using price ratios.
        
        Parameters:
        - original_price_ratio (float): The original price ratio when the liquidity was provided.
        - current_price_ratio (float): The current price ratio of the tokens.
        
        Returns:
        - float: The impermanent loss expressed as a fraction.
        """
        from math import sqrt
        impermanent_loss = 2 * sqrt(current_price_ratio / original_price_ratio) / (1 + current_price_ratio / original_price_ratio) - 1
        return impermanent_loss