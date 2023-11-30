```python
import pandas as pd
from src.pancakeswap_api import get_market_data
from src.oracles import get_price_data
from src.trading_strategies import apply_trading_strategy
from src.config import load_config

class PortfolioBalancer:
    def __init__(self):
        self.config = load_config()
        self.assets = self.config['assets']
        self.portfolio = pd.DataFrame(columns=['asset', 'quantity', 'value'])

    def balance_portfolio(self):
        market_data = get_market_data()
        price_data = get_price_data()

        for asset in self.assets:
            asset_data = market_data[market_data['asset'] == asset]
            asset_price = price_data[price_data['asset'] == asset]['price']
            asset_quantity = self.portfolio[self.portfolio['asset'] == asset]['quantity']

            if not asset_data.empty and not asset_price.empty:
                asset_value = asset_quantity * asset_price
                self.portfolio.loc[self.portfolio['asset'] == asset, 'value'] = asset_value

        total_value = self.portfolio['value'].sum()
        self.portfolio['weight'] = self.portfolio['value'] / total_value

        target_weights = apply_trading_strategy(self.portfolio, market_data)

        rebalance_orders = self._get_rebalance_orders(target_weights)

        return rebalance_orders

    def _get_rebalance_orders(self, target_weights):
        rebalance_orders = []

        for index, row in self.portfolio.iterrows():
            asset = row['asset']
            current_weight = row['weight']
            target_weight = target_weights[asset]

            if current_weight < target_weight:
                rebalance_orders.append({
                    'action': 'BUY',
                    'asset': asset,
                    'quantity': (target_weight - current_weight) * self.portfolio['value'].sum()
                })
            elif current_weight > target_weight:
                rebalance_orders.append({
                    'action': 'SELL',
                    'asset': asset,
                    'quantity': (current_weight - target_weight) * self.portfolio['value'].sum()
                })

        return rebalance_orders
```