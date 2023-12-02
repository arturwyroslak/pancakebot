from time import time

from config import load_config
from pancakeswap_api import PancakeSwapAPI
from web3 import Web3, exceptions

REQUIRED_CONFIG_KEYS = ['blockchain_network', 'private_key', 'pancake_swap_router_address', 'account_address']

class SmartContracts:
    def __init__(self):
        self.config = load_config()
        for key in REQUIRED_CONFIG_KEYS:
            if key not in self.config:
                raise ValueError(f"Missing required configuration key: {key}")
        try:
            self.web3 = Web3(Web3.HTTPProvider(self.config['blockchain_network']))
        except exceptions.InvalidAddress as e:
            raise ValueError("Invalid blockchain network address in configuration.") from e
        self.pancake_swap_api = PancakeSwapAPI()

    def execute_transaction(self, contract_address, function_name, *args):
        contract_abi = self.pancake_swap_api.get_contract_abi(contract_address)
        contract = self.web3.eth.contract(address=contract_address, abi=contract_abi)
        function = contract.get_function_by_name(function_name)
        transaction = function(*args).buildTransaction()
        return self.send_transaction(transaction)

    def send_transaction(self, transaction):
        signed_txn = self.web3.eth.account.signTransaction(transaction, self.config['private_key'])
        return self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    def add_liquidity(self, token_address, amount_token, amount_eth, slippage_tolerance, deadline_offset):
        self.validate_parameters(amount_token, amount_eth, slippage_tolerance, deadline_offset)
        deadline = self.get_blockchain_time() + deadline_offset
        min_amount_token = amount_token * (1 - slippage_tolerance)
        min_amount_eth = amount_eth * (1 - slippage_tolerance)
        return self.execute_transaction(self.config['pancake_swap_router_address'], 'addLiquidityETH', token_address, amount_token, amount_eth, min_amount_token, min_amount_eth, self.config['account_address'], deadline)

    def remove_liquidity(self, token_address, liquidity, amount_token_min, amount_eth_min, slippage_tolerance, deadline_offset):
        self.validate_parameters(liquidity, amount_token_min, amount_eth_min, slippage_tolerance, deadline_offset)
        deadline = self.get_blockchain_time() + deadline_offset
        min_amount_token = amount_token_min * (1 - slippage_tolerance)
        min_amount_eth = amount_eth_min * (1 - slippage_tolerance)
        return self.execute_transaction(self.config['pancake_swap_router_address'], 'removeLiquidityETH', token_address, liquidity, min_amount_token, min_amount_eth, self.config['account_address'], deadline)

    def stake(self, pool_address, amount):
        self.validate_parameters(amount)
        return self.execute_transaction(pool_address, 'stake', amount)

    def unstake(self, pool_address, amount):
        self.validate_parameters(amount)
        return self.execute_transaction(pool_address, 'withdraw', amount)
    def get_blockchain_time(self):
        return self.web3.eth.getBlock('latest')['timestamp']

    def validate_parameters(self, *args):
        for arg in args:
            if arg is None or arg < 0:
                raise ValueError("Invalid parameter value.")
        deadline = int(time.time()) + deadline_offset
        return self.execute_transaction(self.config['pancake_swap_router_address'], 'removeLiquidityETH', token_address, liquidity, amount_token_min * (1 - slippage_tolerance), amount_eth_min * (1 - slippage_tolerance), self.config['account_address'], deadline)

    def stake(self, pool_address, amount):
        return self.execute_transaction(pool_address, 'stake', amount)

    def unstake(self, pool_address, amount):
        return self.execute_transaction(pool_address, 'withdraw', amount)