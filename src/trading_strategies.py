import pandas as pd
from src.pancakeswap_api import get_market_data
from src.oracles import get_price_data
from src.smart_contracts import execute_transaction
from src.config import load_config

import numpy as np
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

        # Simple Moving Average (SMA) Crossover Strategy
        # Calculate the short-term and long-term moving averages (SMA)
        short_window = self.config['short_window']
        long_window = self.config['long_window']
        price_data['short_sma'] = price_data['close'].rolling(window=short_window, min_periods=1).mean()
        price_data['long_sma'] = price_data['close'].rolling(window=long_window, min_periods=1).mean()
        # Generate trading signals: buy when short SMA crosses above long SMA, sell when it crosses below
        price_data['signal'] = 0
        price_data['signal'][short_window:] = np.where(price_data['short_sma'][short_window:] > price_data['long_sma'][short_window:], 1, 0)
        # Compute the difference in signals to find the crossovers
        price_data['positions'] = price_data['signal'].diff()
        # Validate the price data
        if price_data['close'].min() <= 0:
            # In case of invalid price data, we do not trade
            print("Price data is invalid, no transactions will be executed.")
            return
        # Trading execution logic
        if price_data['positions'].iloc[-2] == 1:
            # Buy signal: execute a buy transaction with the configured amount
            execute_transaction('buy', self.config['amount_to_buy'])
        elif price_data['positions'].iloc[-2] == -1:
            # Sell signal: execute a sell transaction with the configured amount
            execute_transaction('sell', self.config['amount_to_sell'])

    def strategy2(self):
        market_data = get_market_data()
        price_data = get_price_data()

        # Relative Strength Index (RSI) Trading Strategy
        # Calculate the RSI
        window_length = self.config['rsi_window_length']
        close = price_data['close']
        delta = close.diff()
        delta = delta[1:]  # Skip the first change, which is NaN
        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0
        roll_up = up.rolling(window_length).mean()
        roll_down = down.abs().rolling(window_length).mean()
        rs = roll_up / roll_down
        rsi = 100 - (100 / (1 + rs))
        # Trading signals based on RSI: overbought and oversold conditions
        overbought_threshold = self.config['rsi_overbought_threshold']
        oversold_threshold = self.config['rsi_oversold_threshold']
        # Validate the price data
        if price_data['close'].min() <= 0:
            # In case of invalid price data, we do not trade
            print("Price data is invalid, no transactions will be executed.")
            return
        # Trading execution logic
        if rsi.iloc[-1] > overbought_threshold:
            # Overbought condition: execute a sell transaction
            execute_transaction('sell', self.config['amount_to_sell'])
        elif rsi.iloc[-1] < oversold_threshold:
            # Oversold condition: execute a buy transaction
            execute_transaction('buy', self.config['amount_to_buy'])

if __name__ == "__main__":
    trading_bot = TradingStrategies()
    trading_bot.apply_trading_strategy('strategy1')