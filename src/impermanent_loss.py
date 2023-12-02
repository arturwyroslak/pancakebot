import math
from src.pancakeswap_api import get_market_data
from src.oracles import get_price_data

def calculate_impermanent_loss(price_change_ratio):
    """
    Calculate impermanent loss given a price change ratio.
    Formula: IL = 2*sqrt(price_change_ratio) / (1+price_change_ratio) - 1
    """
    return 2*math.sqrt(price_change_ratio) / (1+price_change_ratio) - 1

def analyze_impermanent_loss(token1, token2, initial_token1_price, initial_token2_price, pool_share):
    """
    Analyze the impermanent loss for a liquidity pair.
    """
    # Get the current market data
    market_data = get_market_data()

    # Get the current price data from oracles
    price_data = get_price_data()

    # Calculate the price change ratio
    
    # Initial price ratio based on initial prices
    initial_price_ratio = initial_token1_price / initial_token2_price
    
    # Current price ratio based on current prices fetched from oracles
    current_price_ratio = price_data[token1] / price_data[token2]
    
    # Calculate the price change ratio based on the change from the initial state
    price_change_ratio = current_price_ratio / initial_price_ratio

    # Calculate the impermanent loss
    
    # Calculate the gross impermanent loss without considering the owned share of the pool
    gross_impermanent_loss = calculate_impermanent_loss(price_change_ratio)
    # Adjust the impermanent loss based on the pool share owned by the liquidity provider
    impermanent_loss = gross_impermanent_loss * pool_share

    return impermanent_loss