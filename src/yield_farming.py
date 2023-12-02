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
        # Example logic for when to add liquidity
        price_difference_threshold = 0.05 # e.g., 5%
        high_apy_threshold = 10 # e.g., 10%
        current_price_to_target_ratio = pool_price / pool_data['target_price']
        price_spread_significant = abs(1 - current_price_to_target_ratio) > price_difference_threshold
        apy_high = pool_data['apy'] > high_apy_threshold
        if price_spread_significant or apy_high:
            return True
        return False

    def should_remove_liquidity(self, pool_data, pool_price):
        # Example logic for when to remove liquidity
        impermanent_loss_threshold = 0.10 # e.g., 10%
        impermanent_loss = analyze_impermanent_loss(pool_data, pool_price)
        if impermanent_loss > impermanent_loss_threshold:
            return True
        return False

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
        execute_transaction(self.pancake_swap_contract.functions.addLiquidityETH, parameters)

    def remove_liquidity(self, pool):
        # Extract liquidity, minimum amounts, and deadline from the pool config
        liquidity = pool['liquidity']
        amountAMin = pool['amountAMin']
        amountBMin = pool['amountBMin']
        deadline = pool['deadline']
        # Convert them into parameters for PancakeSwap contract interaction
        parameters = [liquidity, amountAMin, amountBMin, deadline]
        # Use the relevant functions from src/smart_contracts.py to build and execute the remove liquidity transaction
        execute_transaction(self.pancake_swap_contract.functions.removeLiquidityETH, parameters)

    def analyze_impermanent_loss(self, pool_data, current_price):
        # Example logic to calculate impermanent loss
        # Assuming we have initial_price from pool_data and a formula to calculate impermanent loss
        initial_price = pool_data['initial_price']
        price_ratio = current_price / initial_price
        # Example formula for impermanent loss calculation (simplified for demonstration)
        impermanent_loss = (2 * (price_ratio ** 0.5) / (1 + price_ratio)) - 1
        return abs(impermanent_loss)