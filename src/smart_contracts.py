```python
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

    def add_liquidity(self, token_address, amount):
        return self.execute_transaction(self.config['pancake_swap_router_address'], 'addLiquidityETH', token_address, amount, 1, 1, self.config['account_address'], int(time.time()) + 1000)

    def remove_liquidity(self, token_address, liquidity):
        return self.execute_transaction(self.config['pancake_swap_router_address'], 'removeLiquidityETH', token_address, liquidity, 1, 1, self.config['account_address'], int(time.time()) + 1000)

    def stake(self, pool_address, amount):
        return self.execute_transaction(pool_address, 'stake', amount)

    def unstake(self, pool_address, amount):
        return self.execute_transaction(pool_address, 'withdraw', amount)
```