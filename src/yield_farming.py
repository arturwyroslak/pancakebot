import json

from src.config import load_config
from src.impermanent_loss import analyze_impermanent_loss
from src.oracles import get_price_data
from src.pancakeswap_api import get_market_data
from src.smart_contracts import execute_transaction
from web3 import Web3


class YieldFarmingManager:
    """
    A class to manage yield farming operations.
    """
    def __init__(self, config=load_config(), web3_provider=Web3.HTTPProvider, contract=Web3.eth.contract):
        """
        Initialize the YieldFarmingManager with the given configuration, web3 provider and contract.

        Parameters:
        - config (dict): The configuration for yield farming.
        - web3_provider (Web3.HTTPProvider): The web3 provider to interact with the blockchain.
        - contract (Web3.eth.contract): The contract to interact with PancakeSwap.
        """
        self.config = config
        self.web3 = Web3(web3_provider(self.config['blockchain_network']))
        self.pancake_swap_contract = contract(address=self.config['pancake_swap_contract_address'], abi=json.loads(self.config['pancake_swap_contract_abi']))

    def manage_yield_farming(self):
        """
        Manage yield farming based on the market data and price data.

        Parameters:
        - get_market_data (function): A function to get the market data.
        - get_price_data (function): A function to get the price data.
        """
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
        """
        Determine whether to add liquidity to the pool based on the pool data and pool price.
    
        Parameters:
        - pool_data (dict): The data of the pool.
        - pool_price (float): The price of the pool.
        - price_difference_threshold (float): The threshold for the price difference to decide whether to add liquidity.
        - high_apy_threshold (float): The threshold for the APY to decide whether to add liquidity.
    
        Returns:
        - bool: True if should add liquidity, False otherwise.
        """
        current_price_to_target_ratio = pool_price / pool_data['target_price']
        price_spread_significant = abs(1 - current_price_to_target_ratio) > price_difference_threshold
        apy_high = pool_data['apy'] > high_apy_threshold
        return price_spread_significant or apy_high

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