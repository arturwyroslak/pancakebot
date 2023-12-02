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
        impermanent_loss = self.analyze_impermanent_loss(pool_data['target_price'], pool_price)
        if impermanent_loss > impermanent_loss_threshold:
            return True
        return False

    def add_liquidity(self, pool):
        # Extract token addresses, amounts, slipperage settings from the pool config
        tokenA = pool.get('tokenA')
        tokenB = pool.get('tokenB')
        amountA = pool.get('amountA')
        amountB = pool.get('amountB')
        slippage = pool.get('slippage', 0.005)  # Default slippage to 0.5% if not provided
        deadline = pool.get('deadline', self.web3.eth.getBlock('latest')['timestamp'] + 300)  # Default deadline to +5min
        if not all([tokenA, tokenB, amountA, amountB]):  # Check if any required parameters are missing
            raise ValueError('Missing required pool parameters for adding liquidity.')
        # Convert them into parameters for PancakeSwap contract interaction
        parameters = [tokenA, tokenB, amountA, amountB, slippage, deadline]
        # Use the relevant functions from src/smart_contracts.py to build and execute the add liquidity transaction
        execute_transaction(self.pancake_swap_contract.functions.addLiquidityETH, parameters)

    def remove_liquidity(self, pool):
        # Extract liquidity, minimum amounts, and deadline from the pool config
        liquidity = pool.get('liquidity')
        amountAMin = pool.get('amountAMin', 0)  # Default to 0 if not provided
        amountBMin = pool.get('amountBMin', 0)  # Default to 0 if not provided
        deadline = pool.get('deadline', self.web3.eth.getBlock('latest')['timestamp'] + 300)  # Default deadline to +5min
        if not liquidity:  # Check if the required liquidity parameter is missing
            raise ValueError('Missing required liquidity parameter for removing liquidity.')
        # Convert them into parameters for PancakeSwap contract interaction
        parameters = [liquidity, amountAMin, amountBMin, deadline]
        # Use the relevant functions from src/smart_contracts.py to build and execute the remove liquidity transaction
        execute_transaction(self.pancake_swap_contract.functions.removeLiquidityETH, parameters)

    def analyze_impermanent_loss(self, original_price, current_price):
        """
        Analyze potential impermanent loss using original and current token prices.
        
        Parameters:
        - original_price (float): The original price of the token when the liquidity was provided.
        - current_price (float): The current price of the token.
        
        Returns:
        - float: The impermanent loss expressed as a fraction.
        
        Note: We handle the case where price ratios could be zero, causing a division by zero error.
        """
        from decimal import Decimal, getcontext
        getcontext().prec = 28  # Precision suitable for financial calculations
        
        
        if original_price == 0 or current_price == 0:
            return Decimal('0')
        original_price_ratio = Decimal(original_price) / Decimal(current_price)
        current_price_ratio = Decimal(current_price) / Decimal(original_price)
        
        impermanent_loss = ((2 * (original_price_ratio * current_price_ratio).sqrt()) / (original_price_ratio + current_price_ratio)) - Decimal('1')

        return impermanent_loss