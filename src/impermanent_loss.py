```python
import math
from src.pancakeswap_api import get_market_data
from src.oracles import get_price_data

def calculate_impermanent_loss(price_change_ratio):
    """
    Calculate impermanent loss given a price change ratio.
    Formula: IL = 2*sqrt(price_change_ratio) / (1+price_change_ratio) - 1
    """
    return 2*math.sqrt(price_change_ratio) / (1+price_change_ratio) - 1

def analyze_impermanent_loss(token1, token2):
    """
    Analyze the impermanent loss for a liquidity pair.
    """
    # Get the current market data
    market_data = get_market_data()

    # Get the current price data from oracles
    price_data = get_price_data()

    # Calculate the price change ratio
    price_change_ratio = price_data[token1] / price_data[token2]

    # Calculate the impermanent loss
    impermanent_loss = calculate_impermanent_loss(price_change_ratio)

    return impermanent_loss
```