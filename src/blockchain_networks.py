python
from web3 import Web3
from src.config import load_config

class BlockchainNetwork:
    def __init__(self):
        self.config = load_config()
        self.networks = self.config['blockchain_networks']
        self.current_network = self.networks['default']
        self.web3 = Web3(Web3.HTTPProvider(self.current_network))

    def switch_network(self, network_name):
        if network_name in self.networks:
            self.current_network = self.networks[network_name]
            self.web3 = Web3(Web3.HTTPProvider(self.current_network))
        else:
            raise ValueError(f"Network {network_name} not found in configuration")

    def get_current_network(self):
        return self.current_network

    def get_web3_instance(self):
        return self.web3
import unittest
from unittest.mock import patch

class TestBlockchainNetwork(unittest.TestCase):
    @patch('src.config.load_config')
    def setUp(self, load_config_mock):
        load_config_mock.return_value = {
            'blockchain_networks': {
                'default': 'http://127.0.0.1:8545',
                'testnet': 'http://127.0.0.1:8546',
                'mainnet': 'https://mainnet.infura.io/v3/your_project_id'
            }
        }
        self.network = BlockchainNetwork()

    def test_switch_network_valid(self):
        self.network.switch_network('testnet')
        self.assertEqual(self.network.get_current_network(), 'http://127.0.0.1:8546')

    def test_switch_network_invalid(self):
        with self.assertRaises(ValueError):
            self.network.switch_network('nonexistent')

if __name__ == '__main__':
    unittest.main()
