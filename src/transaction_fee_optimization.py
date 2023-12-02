```python
from src.config import load_config
from web3 import Web3


class TransactionFeeOptimizer:
    def __init__(self):
        self.config = load_config()
        self.web3 = Web3(Web3.HTTPProvider(self.config['blockchain_network']))

    def get_gas_price(self, speed):
        if speed == 'fast':
            return self.web3.eth.gasPrice * 1.1
        elif speed == 'medium':
            return self.web3.eth.gasPrice
        else:  # slow
            return self.web3.eth.gasPrice * 0.9

    def optimize_transaction_fee(self, transaction, speed='medium'):
        gas_price = self.get_gas_price(speed)
        optimized_fee = self.calculate_optimized_fee(transaction, gas_price)
        if optimized_fee > self.config['max_fee']:
            return self.config['max_fee']
        else:
            return optimized_fee

    def calculate_optimized_fee(self, transaction, gas_price):
        gas_limit = self.estimate_gas_limit(transaction)
        optimized_fee = gas_price * gas_limit
        return optimized_fee

    def estimate_gas_limit(self, transaction):
        return self.web3.eth.estimateGas(transaction)

if __name__ == "__main__":
    optimizer = TransactionFeeOptimizer()
    transaction = {
        'to': '0x0',
        'value': 0,
        'gas': 0,
        'gasPrice': 0,
        'nonce': 0,
        'chainId': 0
    }
    optimized_fee = optimizer.optimize_transaction_fee(transaction)
    print(f"Optimized transaction fee: {optimized_fee}")
```
import unittest
from unittest.mock import MagicMock, patch


class TestTransactionFeeOptimizer(unittest.TestCase):
    @patch('web3.Web3')
    @patch('src.config.load_config')
    def setUp(self, config_mock, web3_mock):
        config_mock.return_value = {'blockchain_network': 'http://localhost:8545', 'max_fee': 100}
        web3_mock.eth.gasPrice = 20
        self.optimizer = TransactionFeeOptimizer()

    def test_get_gas_price(self):
        self.assertEqual(self.optimizer.get_gas_price('fast'), 22)
        self.assertEqual(self.optimizer.get_gas_price('medium'), 20)
        self.assertEqual(self.optimizer.get_gas_price('slow'), 18)

    def test_optimize_transaction_fee(self):
        transaction = {'to': '0x0', 'value': 0, 'gas': 100, 'gasPrice': 0, 'nonce': 0, 'chainId': 0}
        self.assertEqual(self.optimizer.optimize_transaction_fee(transaction, 'fast'), 100)  # max_fee is returned
        self.assertEqual(self.optimizer.optimize_transaction_fee(transaction, 'medium'), 2000)
        self.assertEqual(self.optimizer.optimize_transaction_fee(transaction, 'slow'), 1800)

if __name__ == '__main__':
    unittest.main()