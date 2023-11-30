```python
import unittest
from unittest.mock import patch
from src.reporting import generate_report

class TestReporting(unittest.TestCase):

    @patch('src.reporting.generate_report')
    def test_generate_report(self, mock_generate_report):
        # Mocking the generate_report function
        mock_generate_report.return_value = True

        # Test data
        portfolio_data = {
            'BNB': 10,
            'CAKE': 20,
            'BUSD': 1000
        }

        # Call the function with test data
        result = generate_report(portfolio_data)

        # Assert the function was called with correct parameters
        mock_generate_report.assert_called_with(portfolio_data)

        # Assert the function returned True
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```