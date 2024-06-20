import alpaca_trade_api as tradeapi
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# Replace these with your own API key and secret key
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

# Initialize the Alpaca API
api = tradeapi.REST(API_KEY, SECRET_KEY, base_url='https://paper-api.alpaca.markets')

# Set the symbol and timeframe
symbol = 'AAPL'  # Example: Apple stock
timeframe = '1D'  # Example: 1 day intervals

# Get historical data
historical_data = api.get_bars(symbol, timeframe=timeframe, limit=1000).df

# Print the first few rows of the data
print(historical_data.head())