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

    def train_forecast_model(self, historical_data):
        # Placeholder code - actual implementation will depend on the model choice and data specifics
        # Assuming historical_data is a pandas DataFrame with columns: ['date', 'price']
        X = historical_data['date'].values.reshape(-1, 1)  # Feature (e.g., dates converted to ordinal)
        y = historical_data['price'].values  # Target (prices)
        
        # Example using sklearn (e.g., linear regression model)
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        model.fit(X, y)
        
        # Example using statsmodels (e.g., SARIMA model)
        # import statsmodels.api as sm
        # model = sm.tsa.statespace.SARIMAX(y, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
        # model = model.fit()

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

    def train_simulation_model(self, historical_data):
        # Check that historical_data is not empty and contains the required columns
        if historical_data.empty:
            raise ValueError("Historical data is empty. Cannot train simulation model.")
        if not {'date', 'price'}.issubset(historical_data.columns):
            raise ValueError("Historical data must contain 'date' and 'price' columns.")
        # Convert the 'date' column to numerical values for the model
        historical_data['date_ordinal'] = pd.to_datetime(historical_data['date']).map(lambda x: x.toordinal())
        X = historical_data[['date_ordinal']]  # Features
        y = historical_data['price']  # Target
        # Train a regression model as an example of a simulation model
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        model.fit(X, y)
        # The trained model can be used to predict prices (simulate) for future dates
        return model