```python
import json

from config import load_config
from oracles import Oracle
from pancakeswap_api import PancakeSwapAPI
from smart_contracts import SmartContract
from web3 import Web3


class Staking:
    def __init__(self):
        self.config = load_config()
        self.api = PancakeSwapAPI()
        self.oracle = Oracle()
        self.contract = SmartContract()

    def get_staking_pools(self):
        staking_pools = self.api.get_staking_pools()
        return staking_pools

    def get_pool_data(self, pool_address):
        pool_data = self.api.get_pool_data(pool_address)
        return pool_data

    def stake_tokens(self, pool_address, amount):
        try:
            wei_amount = Web3.toWei(amount, 'ether')
        except ValueError as e:
            print(f"Failed to convert amount to wei: {e}")
            return None
        transaction = self.contract.execute_transaction(
            self.config['wallet_address'],
            pool_address,
            'stake',
            [wei_amount]
        )
        return transaction

    def unstake_tokens(self, pool_address, amount):
        transaction = self.contract.execute_transaction(
            self.config['wallet_address'],
            pool_address,
            'unstake',
            [Web3.toWei(amount, 'ether')]
        )
        return transaction

    def manage_staking(self):
        staking_pools = self.get_staking_pools()
        for pool in staking_pools:
            pool_data = self.get_pool_data(pool['address'])
            if pool_data['apy'] > self.config['min_apy']:
                self.stake_tokens(pool['address'], self.config['stake_amount'])
            elif pool_data['apy'] < self.config['min_apy']:
                self.unstake_tokens(pool['address'], self.config['stake_amount'])
```
import unittest
from unittest.mock import MagicMock, patch


class TestStaking(unittest.TestCase):
    @patch('src.staking.Web3.toWei')
    @patch('src.staking.SmartContract.execute_transaction')
    def test_stake_tokens(self, mock_execute, mock_toWei):
        mock_toWei.return_value = 1000
        staking = Staking()
        staking.stake_tokens('0x...', 1)
        mock_execute.assert_called_once_with(staking.config['wallet_address'], '0x...', 'stake', [1000])

    @patch('src.staking.Web3.toWei')
    @patch('src.staking.SmartContract.execute_transaction')
    def test_unstake_tokens(self, mock_execute, mock_toWei):
        mock_toWei.return_value = 1000
        staking = Staking()
        staking.unstake_tokens('0x...', 1)
        mock_execute.assert_called_once_with(staking.config['wallet_address'], '0x...', 'unstake', [1000])

    @patch('src.staking.Staking.get_staking_pools')
    @patch('src.staking.Staking.get_pool_data')
    @patch('src.staking.Staking.stake_tokens')
    @patch('src.staking.Staking.unstake_tokens')
    def test_manage_staking(self, mock_unstake, mock_stake, mock_get_pool_data, mock_get_staking_pools):
        mock_get_staking_pools.return_value = [{'address': '0x...'}]
        mock_get_pool_data.return_value = {'apy': 15}
        staking = Staking()
        staking.config['min_apy'] = 10
        staking.config['stake_amount'] = 1
        staking.manage_staking()
        mock_stake.assert_called_once_with('0x...', 1)
        mock_unstake.assert_not_called()

if __name__ == '__main__':
    unittest.main()
            if pool_data['apy'] > self.config['min_apy']:
                self.stake_tokens(pool['address'], self.config['stake_amount'])
            elif pool_data['apy'] < self.config['min_apy']:
                self.unstake_tokens(pool['address'], self.config['stake_amount'])
```