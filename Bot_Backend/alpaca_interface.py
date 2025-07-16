import pandas as pd
from alpaca_trade_api.rest import REST
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL, STOCK_SYMBOL, TIMEFRAME

api = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL)


def get_price_data(symbol="AAPL", timeframe="1Day", limit=1000):
    bars = api.get_bars(symbol, timeframe, limit=limit).df
    bars.reset_index(inplace=True)
    bars.rename(columns={'timestamp': 'Date'}, inplace=True)
    return bars
