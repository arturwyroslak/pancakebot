# src/custom_exceptions.py

class MarketDataError(Exception):
    def __init__(self, message="Error fetching market data from PancakeSwap API"):
        self.message = message
        super().__init__(self.message)

class TransactionVolumeError(Exception):
    def __init__(self, message="Error fetching transaction volume data from PancakeSwap API"):
        self.message = message
        super().__init__(self.message)
