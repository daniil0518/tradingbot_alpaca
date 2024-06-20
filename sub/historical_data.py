"""
writen by: BL@CKC@T
telegram: https://t.me/blackcat_919
"""
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Replace these with your own API key and secret key
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

# Initialize the Alpaca API
historical_data_client = StockHistoricalDataClient(api_key=API_KEY, secret_key=SECRET_KEY)

symbol_name='NDAQ'

def get_historical_data(symbol_name, limit=None):
    request_params = StockBarsRequest(
                            symbol_or_symbols=[symbol_name],
                            timeframe=TimeFrame.Hour,
                            start=datetime(2024, 1, 1),
                            limit=limit
                            )

    stock_bars = historical_data_client.get_stock_bars(request_params)
    return stock_bars