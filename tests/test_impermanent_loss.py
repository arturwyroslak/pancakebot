```python
import unittest
from src.impermanent_loss import analyze_impermanent_loss
from src.config import load_config

class TestImpermanentLoss(unittest.TestCase):

    def setUp(self):
        self.config = load_config()

    def test_analyze_impermanent_loss(self):
        # Mocking the price data
        price_data = {
            'token1': 1.0,
            'token2': 0.5
        }

        # Mocking the liquidity pool data
        liquidity_pool_data = {
            'token1': 1000,
            'token2': 2000
        }

        # Expected impermanent loss
        expected_impermanent_loss = 0.057

        # Analyzing the impermanent loss
        impermanent_loss = analyze_impermanent_loss(price_data, liquidity_pool_data, self.config)

        # Asserting the impermanent loss
        self.assertEqual(impermanent_loss, expected_impermanent_loss)

if __name__ == '__main__':
    unittest.main()
```