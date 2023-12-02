import pandas as pd
from src.config import load_config
from src.oracles import Oracle
import sklearn
import statsmodels.api as sm

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
        oracle = Oracle()
        historical_data = oracle.get_price_data(asset)
        return historical_data

    def train_forecast_model(self, historical_data, model_type='linear'):
        # Validate that historical_data is a pandas DataFrame with 'date' and 'price' columns
        if not isinstance(historical_data, pd.DataFrame) or 'date' not in historical_data or 'price' not in historical_data:
            raise ValueError("historical_data must be a pandas DataFrame with 'date' and 'price' columns")

        # Convert 'date' to numerical format for regression analysis
        historical_data['date_ordinal'] = pd.to_datetime(historical_data['date']).apply(lambda x: x.toordinal())

        # Prepare features (X) and target (y)
        X = historical_data['date_ordinal'].values.reshape(-1, 1)
        y = historical_data['price'].values

        # Select the model type
        if model_type == 'linear':
            from sklearn.linear_model import LinearRegression
            model = LinearRegression()
        elif model_type == 'sarima':
            import statsmodels.api as sm
            model = sm.tsa.statespace.SARIMAX(y, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
        else:
            raise ValueError("Unsupported model_type. Choose 'linear' or 'sarima'.")

        # Fit the model
        model = model.fit()

        return model

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

    def train_simulation_model(self, historical_data, simulation_type='monte_carlo'):
        # Validate that historical_data is a pandas DataFrame with at least 'price' column
        if not isinstance(historical_data, pd.DataFrame) or 'price' not in historical_data:
            raise ValueError("historical_data must be a pandas DataFrame with a 'price' column")

        # Prepare target data (y) for simulation
        y = historical_data['price'].values

        # Select the simulation type - using Monte Carlo as an example here
        if simulation_type == 'monte_carlo':
            # Placeholder for Monte Carlo simulation logic
            simulation_model = 'Monte Carlo simulation logic goes here'
        else:
            raise ValueError("Unsupported simulation_type. Example: 'monte_carlo'.")

        # Here, you would implement the logic for training the simulation model based on the historical data
        # As currently, this is placeholder text, it should be replaced with the actual simulation training logic

        return simulation_model