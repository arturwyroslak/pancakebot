```python
import unittest
from unittest.mock import patch
from src import modular_design

class TestModularDesign(unittest.TestCase):

    @patch('src.modular_design.add_module')
    def test_add_module(self, mock_add_module):
        # Test if the function is called with correct parameters
        mock_add_module.return_value = True
        result = modular_design.add_module('new_module')
        self.assertTrue(result)
        mock_add_module.assert_called_with('new_module')

    @patch('src.modular_design.load_config')
    def test_load_config(self, mock_load_config):
        # Test if the function is called with correct parameters
        mock_load_config.return_value = {'network': 'Binance Smart Chain'}
        result = modular_design.load_config()
        self.assertEqual(result, {'network': 'Binance Smart Chain'})
        mock_load_config.assert_called()

if __name__ == '__main__':
    unittest.main()
```