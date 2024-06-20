import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import *
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce, OrderClass



# Replace these with your own API key and secret key
API_KEY = 'PKT3I438NCXYNMA6LTWY'
SECRET_KEY = 'f0us7MRfXfXU4flqd54oRkHMT8uYFZ4qd8Njb5hC'

trading_client = TradingClient(API_KEY, SECRET_KEY)

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url='https://paper-api.alpaca.markets')

# Get our account information.
account = trading_client.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))


# Check our current balance vs. our balance at the last market close
balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')

# search for US equities
search_params = GetAssetsRequest(asset_class=AssetClass.CRYPTO)
assets = trading_client.get_all_assets(search_params)
# print(assets[0])
print(assets[0].name + ' is tradable = ' + str(assets[0].tradable))

asset_symbol = assets[0].symbol
spy_price = api.get_latest_quote('NDAQ')
print(spy_price.bp)
spy_tp = spy_price.bp+(0.05*spy_price.bp)
print (spy_tp)
spy_sl = spy_price.bp-(0.05*spy_price.bp)
print(spy_sl)

# Get a list of all of our positions.
portfolio = trading_client.get_all_positions()

# Print the quantity of shares for each position.
for position in portfolio:
    print("{} shares of {}".format(position.qty, position.symbol))

# print("SPY price: " + str(price))
# preparing bracket order with both stop loss and take profit
bracket__order_data = MarketOrderRequest(
                    symbol="NDAQ",
                    qty=1,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                    order_class=OrderClass.BRACKET,
                    take_profit=TakeProfitRequest(limit_price=round(spy_tp,2)),
                    stop_loss=StopLossRequest(stop_price=round(spy_sl,2))
                    )

bracket_order = trading_client.submit_order(
                order_data=bracket__order_data
               )

# print(bracket_order)


# # preparing market order
# market_order_data = MarketOrderRequest(
#                     symbol="SPY",
#                     qty=0.023,
#                     side=OrderSide.BUY,
#                     time_in_force=TimeInForce.DAY
#                     )
#
# # Market order
# market_order = trading_client.submit_order(
#                 order_data=market_order_data
#                )
#
# print(market_order)