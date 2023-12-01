```python
import requests
from src.config import PANCAKESWAP_API_URL

class PancakeSwapAPI:
    def __init__(self):
        self.api_url = PANCAKESWAP_API_URL

    def get_market_data(self):
        """
        Fetches real-time market data from PancakeSwap API.
        """
        try:
            response = requests.get(f"{self.api_url}/market-data")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")

    def get_liquidity_data(self):
        """
        Fetches liquidity data from PancakeSwap API.
        """
        try:
            response = requests.get(f"{self.api_url}/liquidity-data")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")

    def get_transaction_volume(self):
        """
        Fetches transaction volume data from PancakeSwap API.
        """
        try:
            response = requests.get(f"{self.api_url}/transaction-volume")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")
```