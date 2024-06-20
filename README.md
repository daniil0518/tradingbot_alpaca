
# Automated Trading Bot using Moving Average Crossover Strategy

## Overview
This project implements an automated trading bot in Python that utilizes a moving average crossover strategy to make buy/sell decisions in financial markets. The bot is designed to execute trades based on the crossing of short-term and long-term moving averages, a popular strategy used by traders to identify potential trend reversals.

## Features
- Fetches real-time market data using the Alpaca API.
- Calculates short-term and long-term moving averages of asset prices.
- Generates buy signals when the short-term moving average crosses above the long-term moving average.
- Generates sell signals when the short-term moving average crosses below the long-term moving average.
- Implements risk management measures to control position sizing and minimize losses.
- Provides backtesting functionality to evaluate the bot's performance using historical data.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/daniil0518/tradingbot_alpaca.git
   cd tradingbot_alpaca
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Obtain API keys:
   - Sign up for an account on Alpaca and obtain your API key and secret key.

4. Update configuration:
   - Replace `'your_api_key'` and `'your_secret_key'` in the code with your actual Alpaca API key and secret key.

5. Run the bot:
   ```bash
   python main.py
   ```

## Usage
- Customize the asset symbol and moving average periods in the code according to your preferences.
- Monitor the bot's output to receive buy/sell signals and execute trades accordingly.
- Backtest the bot's performance using historical data to evaluate its effectiveness.

## Acknowledgements
- This project utilizes the [Alpaca API](https://alpaca.markets/docs/api-documentation/) for accessing real-time market data and executing trades.

## Disclaimer
- This project is for educational and informational purposes only. Automated trading bots involve risks, and past performance is not indicative of future results. Use at your own risk.

---
