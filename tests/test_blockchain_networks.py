```python
import unittest
from unittest.mock import patch
from src.blockchain_networks import switch_blockchain_network

class TestBlockchainNetworks(unittest.TestCase):

    @patch('src.blockchain_networks.switch_blockchain_network')
    def test_switch_blockchain_network(self, mock_switch):
        # Test switching to a valid network
        mock_switch.return_value = True
        result = switch_blockchain_network('Ethereum')
        self.assertTrue(result)

        # Test switching to an invalid network
        mock_switch.return_value = False
        result = switch_blockchain_network('InvalidNetwork')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
```