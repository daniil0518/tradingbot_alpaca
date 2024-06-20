"""
writen by: BL@CKC@T
telegram: https://t.me/blackcat_919
"""
from alpaca.trading.requests import MarketOrderRequest, TakeProfitRequest, StopLossRequest
from alpaca.trading.enums import OrderSide, TimeInForce, OrderClass

def execute_buy_order(trading_client, symbol, tp_price, sl_price):
    bracket__order_data = MarketOrderRequest(
        symbol=symbol,
        qty=1,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY,
        order_class=OrderClass.BRACKET,
        take_profit=TakeProfitRequest(limit_price=round(tp_price, 2)),
        stop_loss=StopLossRequest(stop_price=round(sl_price, 2))
    )

    bracket_order = trading_client.submit_order(
        order_data=bracket__order_data
    )
    return None


def execute_sell_order(trading_client, symbol, tp_price, sl_price):
    bracket__order_data = MarketOrderRequest(
        symbol=symbol,
        qty=1,
        side=OrderSide.SELL,
        time_in_force=TimeInForce.DAY,
        order_class=OrderClass.BRACKET,
        take_profit=TakeProfitRequest(limit_price=round(tp_price, 2)),
        stop_loss=StopLossRequest(stop_price=round(sl_price, 2))
    )

    bracket_order = trading_client.submit_order(
        order_data=bracket__order_data
    )
    return None
