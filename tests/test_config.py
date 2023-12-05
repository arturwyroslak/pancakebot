import unittest
from src import config

class TestConfig(unittest.TestCase):

    def setUp(self):
        self.config = config.load_config()

    def test_config_loaded(self):
        self.assertIsNotNone(self.config, "Failed to load config")

    def test_pancakeswap_api_url(self):
        self.assertIn('pancakeswap_api_url', self.config, "PancakeSwap API URL not found in config")

    def test_oracle_api_url(self):
        self.assertIn('oracle_api_url', self.config, "Oracle API URL not found in config")

    def test_smart_contract_address(self):
        self.assertIn('smart_contract_address', self.config, "Smart contract address not found in config")

    def test_trading_algorithm(self):
        self.assertIn('trading_algorithm', self.config, "Trading algorithm not found in config")

    def test_yield_farming_strategy(self):
        self.assertIn('yield_farming_strategy', self.config, "Yield farming strategy not found in config")

    def test_defi_contract_address(self):
        self.assertIn('defi_contract_address', self.config, "DeFi contract address not found in config")

    def test_security_level(self):
        self.assertIn('security_level', self.config, "Security level not found in config")

    def test_portfolio_balancing_strategy(self):
        self.assertIn('portfolio_balancing_strategy', self.config, "Portfolio balancing strategy not found in config")

    def test_ui_level(self):
        self.assertIn('ui_level', self.config, "UI level not found in config")

    def test_transaction_fee_optimization(self):
        self.assertIn('transaction_fee_optimization', self.config, "Transaction fee optimization not found in config")

    def test_blockchain_network(self):
        self.assertIn('blockchain_network', self.config, "Blockchain network not found in config")

    def test_modular_design(self):
        self.assertIn('modular_design', self.config, "Modular design not found in config")

if __name__ == '__main__':
    unittest.main()
