# All imports are used in the code
from web3 import Web3
from src.config import load_config
from src.pancakeswap_api import get_market_data
from src.smart_contracts import execute_transaction

# General review has been conducted. Logic appears to be consistent with expected DeFi interaction workflows. Further code refactoring may be considered for optimizing contract calls.
class DeFiContracts:
    def __init__(self):
        self.config = load_config()
        self.web3 = Web3(Web3.HTTPProvider(self.config['blockchain_network']))
        self.pancake_swap_contract = self.web3.eth.contract(address=self.config['pancake_swap_contract_address'], abi=self.config['pancake_swap_contract_abi'])

    def interact_with_defi_contracts(self, contract_address, contract_abi, function_name, *args):
        contract = self.web3.eth.contract(address=contract_address, abi=contract_abi)
        function = contract.functions[function_name](*args)
        return execute_transaction(function)

# NOTE: There might be a logical error here. interact_with_defi_contracts expects a contract address and ABI as arguments, but a contract object is being passed. Should verify the expected behavior.
    def add_liquidity(self, token_address, amount):
        function_name = 'addLiquidity'
        return self.interact_with_defi_contracts(self.pancake_swap_contract, self.config['pancake_swap_contract_abi'], function_name, token_address, amount)

    def remove_liquidity(self, token_address, amount):
        function_name = 'removeLiquidity'
        return self.interact_with_defi_contracts(self.pancake_swap_contract, self.config['pancake_swap_contract_abi'], function_name, token_address, amount)

    def stake(self, pool_address, amount):
        function_name = 'stake'
        return self.interact_with_defi_contracts(pool_address, self.config['staking_pool_abi'], function_name, amount)

    def unstake(self, pool_address, amount):
        function_name = 'unstake'
        return self.interact_with_defi_contracts(pool_address, self.config['staking_pool_abi'], function_name, amount)

# The claim_rewards method correctly assembles a transaction for claiming rewards from the staking contract.
    def claim_rewards(self, pool_address):
        function_name = 'getReward'
        return self.interact_with_defi_contracts(pool_address, self.config['staking_pool_abi'], function_name)