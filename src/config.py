# Configuration file for PancakeSwap Profit Maximizing Bot

# PancakeSwap API configuration
PANCAKESWAP_API_URL = "https://api.pancakeswap.com/api/v1/"

# Oracle configuration
ORACLE_API_URL = "https://oracleapi.com/"

# Smart Contract configuration
SMART_CONTRACT_ADDRESS = "0x..."

# Trading Algorithm configuration
TRADING_ALGORITHM = "MACD"  # Moving Average Convergence Divergence

# Yield Farming and Staking configuration
YIELD_FARMING_STRATEGY = "highest_apr"  # Strategy based on highest Annual Percentage Rate
STAKING_STRATEGY = "highest_rewards"  # Strategy based on highest rewards

# DeFi Contracts configuration
DEFI_CONTRACT_ADDRESS = "0x..."

# Security configuration
SECURITY_LEVEL = "high"  # High level of security measures

# Portfolio Balancing configuration
PORTFOLIO_BALANCING_STRATEGY = "diversified"  # Diversified portfolio strategy

# User Interface configuration
UI_LEVEL = "advanced"  # Advanced level of user interface

# Transaction Fee Optimization configuration
TRANSACTION_FEE_OPTIMIZATION = True  # Enable transaction fee optimization

# Blockchain Networks configuration
blockchain_networks = {
    "default": "https://bsc-dataseed.binance.org/",
    "ethereum": "https://mainnet.infura.io/v3/your_project_id",
    "binance_smart_chain": "https://bsc-dataseed.binance.org/",
    "polygon": "https://rpc-mainnet.maticvigil.com/"
}

# Modular Design configuration
MODULAR_DESIGN = True  # Enable modular design

# Load the configuration
def load_config():
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