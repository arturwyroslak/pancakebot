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
        try:
            market_data = get_market_data()
            messagebox.showinfo("Market Data", market_data)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_price_data(self):
        try:
            price_data = get_price_data()
            messagebox.showinfo("Price Data", price_data)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def apply_strategy(self):
        try:
            apply_trading_strategy()
            messagebox.showinfo("Success", "Trading strategy applied successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def balance_portfolio(self):
        try:
            balance_portfolio()
            messagebox.showinfo("Success", "Portfolio balanced successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_report(self):
        try:
            report = generate_report()
            messagebox.showinfo("Report", report)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.create_widgets()
        self.root.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
```
    def validate_config(self):
        try:
            # Validate loaded configuration
            if not self.config:
                messagebox.showerror("Error", "Configuration not loaded.")
                return False
            if "api_key" not in self.config:
                messagebox.showerror("Error", "API key not found in configuration.")
                return False
            # Add more validation checks if needed
            return True
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return False

    def update_ui(self, message):
        messagebox.showinfo("Message", message)