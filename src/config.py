# Configuration file for PancakeSwap Profit Maximizing Bot

# PancakeSwap API configuration
# The URL is used to interact with the PancakeSwap API for trading operations
PANCAKESWAP_API_URL = os.getenv('PANCAKESWAP_API_URL', "https://api.pancakeswap.com/api/v1/")

# Oracle configuration
# The URL is used to interact with the Oracle API for price feed
ORACLE_API_URL = os.getenv('ORACLE_API_URL', "https://oracleapi.com/")

# Smart Contract configuration
# The address of the smart contract to interact with for trading operations
SMART_CONTRACT_ADDRESS = os.getenv('SMART_CONTRACT_ADDRESS', "0x...")

# Trading Algorithm configuration
TRADING_ALGORITHM = "MACD"  # Moving Average Convergence Divergence

# Yield Farming and Staking configuration
YIELD_FARMING_STRATEGY = "highest_apr"  # Strategy based on highest Annual Percentage Rate
STAKING_STRATEGY = "highest_rewards"  # Strategy based on highest rewards

# DeFi Contracts configuration
DEFI_CONTRACT_ADDRESS = "0x..."

# Security configuration
SECURITY_LEVEL = "high"  # High level of security measures
# The level of security measures to be applied in the bot operations
SECURITY_LEVEL = os.getenv('SECURITY_LEVEL', "high")  # High level of security measures

# Portfolio Balancing configuration
# The strategy used for portfolio balancing
PORTFOLIO_BALANCING_STRATEGY = os.getenv('PORTFOLIO_BALANCING_STRATEGY', "diversified")  # Diversified portfolio strategy

# User Interface configuration
# The level of user interface complexity
UI_LEVEL = os.getenv('UI_LEVEL', "advanced")  # Advanced level of user interface

# Transaction Fee Optimization configuration
# Enable or disable transaction fee optimization
TRANSACTION_FEE_OPTIMIZATION = os.getenv('TRANSACTION_FEE_OPTIMIZATION', True)  # Enable transaction fee optimization


BLOCKCHAIN_NETWORK = os.getenv('BLOCKCHAIN_NETWORK', "Binance_Smart_Chain")  # Default blockchain network


# Modular Design configuration
# Enable or disable modular design
MODULAR_DESIGN = os.getenv('MODULAR_DESIGN', True)  # Enable modular design

# Load the configuration
def load_config():

def load_config():
    # This function loads the configuration from environment variables and returns a dictionary
    config = {
        "pancakeswap_api_url": PANCAKESWAP_API_URL,
        "oracle_api_url": ORACLE_API_URL,
        "smart_contract_address": SMART_CONTRACT_ADDRESS,
        "trading_algorithm": TRADING_ALGORITHM,
        "yield_farming_strategy": YIELD_FARMING_STRATEGY,
        "staking_strategy": STAKING_STRATEGY,
        "defi_contract_address": DEFI_CONTRACT_ADDRESS,
        "security_level": SECURITY_LEVEL,
        "portfolio_balancing_strategy": PORTFOLIO_BALANCING_STRATEGY,
        "ui_level": UI_LEVEL,
        "transaction_fee_optimization": TRANSACTION_FEE_OPTIMIZATION,
        "blockchain_networks": blockchain_networks,
        "modular_design": MODULAR_DESIGN
    }
    return config