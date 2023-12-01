```python
import tkinter as tk
from tkinter import ttk
from src.config import load_config
from src.pancakeswap_api import get_market_data
from src.oracles import get_price_data
from src.trading_strategies import apply_trading_strategy
from src.portfolio_balancing import balance_portfolio
from src.reporting import generate_report

class UserInterface:
    def __init__(self):
        self.config = load_config()
        self.root = tk.Tk()
        self.root.title("PancakeSwap Profit Maximizing Bot")

    def create_widgets(self):
        market_data_button = ttk.Button(self.root, text="Get Market Data", command=self.display_market_data)
        market_data_button.pack()

        price_data_button = ttk.Button(self.root, text="Get Price Data", command=self.display_price_data)
        price_data_button.pack()

        trading_strategy_button = ttk.Button(self.root, text="Apply Trading Strategy", command=self.apply_strategy)
        trading_strategy_button.pack()

        portfolio_balancing_button = ttk.Button(self.root, text="Balance Portfolio", command=self.balance_portfolio)
        portfolio_balancing_button.pack()

        report_button = ttk.Button(self.root, text="Generate Report", command=self.generate_report)
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