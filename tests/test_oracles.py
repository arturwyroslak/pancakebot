```python
import unittest
from unittest.mock import patch
from src import oracles

class TestOracles(unittest.TestCase):

    @patch('src.oracles.get_price_data')
    def test_get_price_data(self, mock_get_price_data):
        # Arrange
        mock_get_price_data.return_value = 100

        # Act
        result = oracles.get_price_data('BTC')

        # Assert
        self.assertEqual(result, 100)
        mock_get_price_data.assert_called_once_with('BTC')

    @patch('src.oracles.get_price_data')
    def test_get_price_data_invalid_token(self, mock_get_price_data):
        # Arrange
        mock_get_price_data.return_value = None

        # Act
        result = oracles.get_price_data('INVALID')

        # Assert
        self.assertEqual(result, None)
        mock_get_price_data.assert_called_once_with('INVALID')

if __name__ == '__main__':
    unittest.main()
```