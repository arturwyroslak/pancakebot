```python
import tkinter as tk
from tkinter import ttk

from src.config import load_config
from src.oracles import get_price_data
from src.pancakeswap_api import get_market_data
from src.portfolio_balancing import balance_portfolio
from src.reporting import generate_report
from src.trading_strategies import apply_trading_strategy


class UserInterface:
    def __init__(self):
        self.config = load_config()
        self.root = tk.Tk()
        self.root.title("PancakeSwap Profit Maximizing Bot")

    def create_widgets(self):
        market_data_button = ttk.Button(self.root, text="Get Market Data", command=self.display_market_data_wrapper)
        market_data_button.pack()

        price_data_button = ttk.Button(self.root, text="Get Price Data", command=self.display_price_data_wrapper)
        price_data_button.pack()

        trading_strategy_button = ttk.Button(self.root, text="Apply Trading Strategy", command=self.apply_strategy_wrapper)
        trading_strategy_button.pack()

        portfolio_balancing_button = ttk.Button(self.root, text="Balance Portfolio", command=self.balance_portfolio_wrapper)
        portfolio_balancing_button.pack()

        report_button = ttk.Button(self.root, text="Generate Report", command=self.generate_report_wrapper)
        report_button.pack()

    def display_market_data(self):
        market_data = get_market_data()
        print(market_data)

    def display_price_data(self):
        price_data = get_price_data()
        print(price_data)

    def apply_strategy(self):
        apply_trading_strategy()

    def balance_portfolio(self):
        balance_portfolio()

    def generate_report(self):
        report = generate_report()
        print(report)

    def run(self):
        self.create_widgets()
        self.root.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
```
import unittest
from unittest.mock import MagicMock, patch


class TestUserInterface(unittest.TestCase):
    @patch('src.user_interface.load_config')
    @patch('src.user_interface.get_market_data')
    @patch('src.user_interface.get_price_data')
    @patch('src.user_interface.apply_trading_strategy')
    @patch('src.user_interface.balance_portfolio')
    @patch('src.user_interface.generate_report')
    def setUp(self, generate_report_mock, balance_portfolio_mock, apply_trading_strategy_mock, get_price_data_mock, get_market_data_mock, load_config_mock):
        load_config_mock.return_value = {}
        get_market_data_mock.return_value = "Market Data"
        get_price_data_mock.return_value = "Price Data"
        apply_trading_strategy_mock.return_value = "Strategy Applied"
        balance_portfolio_mock.return_value = "Portfolio Balanced"
        generate_report_mock.return_value = "Report Generated"
        self.ui = UserInterface()

    def test_display_market_data(self):
        self.ui.display_market_data_wrapper()
        self.assertEqual(self.ui.market_data_label['text'], "Market Data")

    def test_display_price_data(self):
        self.ui.display_price_data_wrapper()
        self.assertEqual(self.ui.price_data_label['text'], "Price Data")

    def test_apply_strategy(self):
        self.ui.apply_strategy_wrapper()
        self.assertEqual(self.ui.strategy_label['text'], "Strategy Applied")

    def test_balance_portfolio(self):
        self.ui.balance_portfolio_wrapper()
        self.assertEqual(self.ui.portfolio_label['text'], "Portfolio Balanced")

    def test_generate_report(self):
        self.ui.generate_report_wrapper()
        self.assertEqual(self.ui.report_label['text'], "Report Generated")

if __name__ == "__main__":
    unittest.main()
import unittest
from unittest.mock import MagicMock, patch


class TestUserInterface(unittest.TestCase):
    @patch('src.user_interface.load_config')
    @patch('src.user_interface.get_market_data')
    @patch('src.user_interface.get_price_data')
    @patch('src.user_interface.apply_trading_strategy')
    @patch('src.user_interface.balance_portfolio')
    @patch('src.user_interface.generate_report')
    def setUp(self, generate_report_mock, balance_portfolio_mock, apply_trading_strategy_mock, get_price_data_mock, get_market_data_mock, load_config_mock):
        load_config_mock.return_value = {}
        get_market_data_mock.return_value = "Market Data"
        get_price_data_mock.return_value = "Price Data"
        apply_trading_strategy_mock.return_value = "Strategy Applied"
        balance_portfolio_mock.return_value = "Portfolio Balanced"
        generate_report_mock.return_value = "Report Generated"
        self.ui = UserInterface()

    def test_display_market_data(self):
        self.ui.display_market_data_wrapper()
        self.assertEqual(self.ui.market_data_label['text'], "Market Data")

    def test_display_price_data(self):
        self.ui.display_price_data_wrapper()
        self.assertEqual(self.ui.price_data_label['text'], "Price Data")

    def test_apply_strategy(self):
        self.ui.apply_strategy_wrapper()
        self.assertEqual(self.ui.strategy_label['text'], "Strategy Applied")

    def test_balance_portfolio(self):
        self.ui.balance_portfolio_wrapper()
        self.assertEqual(self.ui.portfolio_label['text'], "Portfolio Balanced")

    def test_generate_report(self):
        self.ui.generate_report_wrapper()
        self.assertEqual(self.ui.report_label['text'], "Report Generated")

if __name__ == "__main__":
    unittest.main()
import unittest
from unittest.mock import MagicMock, patch


class TestUserInterface(unittest.TestCase):
    @patch('src.user_interface.load_config')
    @patch('src.user_interface.get_market_data')
    @patch('src.user_interface.get_price_data')
    @patch('src.user_interface.apply_trading_strategy')
    @patch('src.user_interface.balance_portfolio')
    @patch('src.user_interface.generate_report')
    def setUp(self, generate_report_mock, balance_portfolio_mock, apply_trading_strategy_mock, get_price_data_mock, get_market_data_mock, load_config_mock):
        load_config_mock.return_value = {}
        get_market_data_mock.return_value = "Market Data"
        get_price_data_mock.return_value = "Price Data"
        apply_trading_strategy_mock.return_value = "Strategy Applied"
        balance_portfolio_mock.return_value = "Portfolio Balanced"
        generate_report_mock.return_value = "Report Generated"
        self.ui = UserInterface()

    def test_display_market_data(self):
        self.ui.display_market_data_wrapper()
        self.assertEqual(self.ui.market_data_label['text'], "Market Data")

    def test_display_price_data(self):
        self.ui.display_price_data_wrapper()
        self.assertEqual(self.ui.price_data_label['text'], "Price Data")

    def test_apply_strategy(self):
        self.ui.apply_strategy_wrapper()
        self.assertEqual(self.ui.strategy_label['text'], "Strategy Applied")

    def test_balance_portfolio(self):
        self.ui.balance_portfolio_wrapper()
        self.assertEqual(self.ui.portfolio_label['text'], "Portfolio Balanced")

    def test_generate_report(self):
        self.ui.generate_report_wrapper()
        self.assertEqual(self.ui.report_label['text'], "Report Generated")

if __name__ == "__main__":
    unittest.main()
            portfolio = balance_portfolio()
            self.portfolio_label = tk.Label(self.root, text=portfolio)
            self.portfolio_label.pack()
        except Exception as e:
            print(f"Error balancing portfolio: {e}")

    def generate_report_wrapper(self):
        try:
            report = generate_report()
            self.report_label = tk.Label(self.root, text=report)
            self.report_label.pack()
        except Exception as e:
            print(f"Error generating report: {e}")

    def run(self):
        self.create_widgets()
        self.root.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
```