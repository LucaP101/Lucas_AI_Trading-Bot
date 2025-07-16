import pandas as pd
import data_handler
import model_training
import alpaca_interface

def run_backtest(symbol, timeframe, num_days):
    df = alpaca_interface.get_price_data(symbol, timeframe, num_days)
    df = data_handler.add_indicators(df)
    df = df.dropna().reset_index(drop=True)

    equity = 10000  # starting cash
    balance_history = []
    trades = []

    for i in range(60, len(df)-1):
        train_data = df.iloc[:i]
        model = model_training.train_model(train_data)

        features = df.iloc[i][['Return', 'MA10', 'RSI']].values.reshape(1, -1)
        prediction = model.predict(features)[0]

        today_close = df.iloc[i]['close']
        tomorrow_close = df.iloc[i+1]['close']
        date = df.iloc[i+1]['Date']

        if prediction == 1:
            pct_return = (tomorrow_close - today_close) / today_close
            profit = equity * pct_return
            equity += profit

            trades.append({
                'Date': date,
                'Buy_Price': today_close,
                'Sell_Price': tomorrow_close,
                'Pct_Return': pct_return,
                'Profit': profit,
                'Equity': equity
            })
        else:
            trades.append({
                'Date': date,
                'Buy_Price': None,
                'Sell_Price': None,
                'Pct_Return': 0,
                'Profit': 0,
                'Equity': equity
            })

        balance_history.append(equity)

    df_results = pd.DataFrame(trades)
    print(df_results.tail(10))

    total_return = (equity - 10000) / 10000
    annualized_return = ((1 + total_return) ** (252 / len(trades))) - 1

    print("\n✅ Backtest Summary:")
    print(f"Total Return: {round(total_return * 100, 2)}%")
    print(f"Annualized Return: {round(annualized_return * 100, 2)}%")
    print(f"Final Equity: ${round(equity, 2)}")

if __name__ == "__main__":
    run_backtest("AAPL", "1Day", 1500)
    df = alpaca_interface.get_price_data("AAPL", "1Day", 1500)
    df = data_handler.add_indicators(df)
    df = df.dropna().reset_index(drop=True)

    equity = 10000  # starting cash
    balance_history = []
    trades = []

    for i in range(60, len(df)-1):
        train_data = df.iloc[:i]
        model = model_training.train_model(train_data)

        features = df.iloc[i][['Return', 'MA10', 'RSI']].values.reshape(1, -1)
        prediction = model.predict(features)[0]

        today_close = df.iloc[i]['close']
        tomorrow_close = df.iloc[i+1]['close']
        date = df.iloc[i+1]['Date']

        if prediction == 1:
            pct_return = (tomorrow_close - today_close) / today_close
            profit = equity * pct_return
            equity += profit

            trades.append({
                'Date': date,
                'Buy_Price': today_close,
                'Sell_Price': tomorrow_close,
                'Pct_Return': pct_return,
                'Profit': profit,
                'Equity': equity
            })
        else:
            trades.append({
                'Date': date,
                'Buy_Price': None,
                'Sell_Price': None,
                'Pct_Return': 0,
                'Profit': 0,
                'Equity': equity
            })

        balance_history.append(equity)

    df_results = pd.DataFrame(trades)
    print(df_results.tail(10))

    total_return = (equity - 10000) / 10000
    annualized_return = ((1 + total_return) ** (252 / len(trades))) - 1

    print("\n✅ Backtest Summary:")
    print(f"Total Return: {round(total_return * 100, 2)}%")
    print(f"Annualized Return: {round(annualized_return * 100, 2)}%")
    print(f"Final Equity: ${round(equity, 2)}")

if __name__ == "__main__":
    run_backtest()
