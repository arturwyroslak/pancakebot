```python
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
```