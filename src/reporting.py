```python
import pandas as pd
from src.config import load_config

class Reporting:
    def __init__(self):
        self.config = load_config()

    def generate_report(self, portfolio):
        report = pd.DataFrame(portfolio)
        report['Value'] = report['Amount'] * report['Price']
        total_value = report['Value'].sum()
        report['Percentage'] = report['Value'] / total_value * 100
        return report

    def generate_forecast(self, portfolio, forecast_period):
        forecast = {}
        for asset in portfolio:
            forecast[asset] = self.forecast_asset(asset, forecast_period)
        return forecast

    def forecast_asset(self, asset, forecast_period):
        historical_data = self.get_historical_data(asset)
        forecast_model = self.train_forecast_model(historical_data)
        forecast = forecast_model.predict(forecast_period)
        return forecast

    def get_historical_data(self, asset):
        # This function should be implemented to fetch historical data for the given asset
        pass

    def train_forecast_model(self, historical_data):
        # This function should be implemented to train a forecast model using the historical data
        pass

    def generate_simulation(self, portfolio, simulation_period):
        simulation = {}
        for asset in portfolio:
            simulation[asset] = self.simulate_asset(asset, simulation_period)
        return simulation

    def simulate_asset(self, asset, simulation_period):
        historical_data = self.get_historical_data(asset)
        simulation_model = self.train_simulation_model(historical_data)
        simulation = simulation_model.simulate(simulation_period)
        return simulation

    def train_simulation_model(self, historical_data):
        # This function should be implemented to train a simulation model using the historical data
        pass
```