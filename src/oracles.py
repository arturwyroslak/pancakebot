import requests
import json
from src.config import ORACLE_API_URLS

class Oracle:
    def __init__(self):
        self.oracles = ORACLE_API_URLS

    def get_price_data(self, token):
        price_data = {}
        for oracle_name, oracle_url in self.oracles.items():
            try:
                response = requests.get(oracle_url.format(token))
                response.raise_for_status()
                data = response.json()
                if 'price' in data:
                    price_data[oracle_name] = data['price']
                else:
                    print(f"'price' key is missing in the data from {oracle_name}")
            except requests.exceptions.RequestException as err:
                print(f"Error fetching price data from {oracle_name}: {err}")
            except json.JSONDecodeError as err:
                print(f"JSON decoding error from {oracle_name}: {err}")
        return price_data