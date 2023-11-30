```python
import pandas as pd
from src.pancakeswap_api import get_market_data
from src.oracles import get_price_data
from src.smart_contracts import execute_transaction
from src.config import load_config

class TradingStrategies:
    def __init__(self):
        self.config = load_config()

    def apply_trading_strategy(self, strategy):
        if strategy == 'strategy1':
            self.strategy1()
        elif strategy == 'strategy2':
            self.strategy2()
        else:
            print("Invalid strategy")

    def strategy1(self):
        market_data = get_market_data()
        price_data = get_price_data()

        # Implement your trading strategy here
        # This is a placeholder for your trading strategy
        # You can use market_data and price_data to make trading decisions

        # Example: If the current price is lower than the average price, buy the token
        if price_data['current_price'] < price_data['average_price']:
            execute_transaction('buy', self.config['amount_to_buy'])

    def strategy2(self):
        market_data = get_market_data()
        price_data = get_price_data()

        # Implement your trading strategy here
        # This is a placeholder for your trading strategy
        # You can use market_data and price_data to make trading decisions

        # Example: If the current price is higher than the average price, sell the token
        if price_data['current_price'] > price_data['average_price']:
            execute_transaction('sell', self.config['amount_to_sell'])

if __name__ == "__main__":
    trading_bot = TradingStrategies()
    trading_bot.apply_trading_strategy('strategy1')
```