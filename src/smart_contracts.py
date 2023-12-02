from time import time
from web3 import Web3
from pancakeswap_api import PancakeSwapAPI
from config import load_config

class SmartContracts:
    def __init__(self):
        self.config = load_config()
        self.web3 = Web3(Web3.HTTPProvider(self.config['blockchain_network']))
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
        deadline = int(time.time()) + deadline_offset
        return self.execute_transaction(self.config['pancake_swap_router_address'], 'addLiquidityETH', token_address, amount_token, amount_eth, amount_token * (1 - slippage_tolerance), amount_eth * (1 - slippage_tolerance), self.config['account_address'], deadline)

    def remove_liquidity(self, token_address, liquidity, amount_token_min, amount_eth_min, slippage_tolerance, deadline_offset):
        deadline = int(time.time()) + deadline_offset
        return self.execute_transaction(self.config['pancake_swap_router_address'], 'removeLiquidityETH', token_address, liquidity, amount_token_min * (1 - slippage_tolerance), amount_eth_min * (1 - slippage_tolerance), self.config['account_address'], deadline)

    def stake(self, pool_address, amount):
        return self.execute_transaction(pool_address, 'stake', amount)

    def unstake(self, pool_address, amount):
        return self.execute_transaction(pool_address, 'withdraw', amount)