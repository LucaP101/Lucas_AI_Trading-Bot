import pandas as pd
from alpaca_trade_api.rest import REST
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL, STOCK_SYMBOL, TIMEFRAME

api = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL)

def get_price_data(limit=100):
    bars = api.get_bars(STOCK_SYMBOL, TIMEFRAME, limit=limit).df
    return bars
