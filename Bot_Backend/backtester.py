import pandas as pd
import data_handler
import model_training
import alpaca_interface

def run_backtest(symbol, timeframe, num_days):
    df = alpaca_interface.get_price_data(symbol, timeframe, num_days)
    df = data_handler.add_indicators(df)
    df = df.dropna().reset_index(drop=True)
    print(f"📊 Final data size after indicators: {len(df)} rows")

    equity = 10000
    trades = []
    biggest_loss = 0

    for i in range(60, len(df)-1):
        train_data = df.iloc[:i]
        model = model_training.train_model(train_data)

        features = df.iloc[i][['Return', 'MA10', 'RSI']].values.reshape(1, -1)
        prediction = model.predict(features)[0]

        if prediction == 1:
            today = df.iloc[i]['close']
            tomorrow = df.iloc[i+1]['close']
            pct_return = (tomorrow - today) / today
            profit = equity * pct_return
            equity += profit
            trades.append(profit)

            if profit < biggest_loss:
                biggest_loss = profit

    total_profit = equity - 10000
    print("✅ Simple Backtest Results")
    print(f"Days Tested: {len(df) - 60}")
    print(f"Number of Trades: {len(trades)}")
    print(f"Total Profit: ${round(total_profit, 2)}")
    print(f"Biggest Single Loss: ${round(biggest_loss, 2)}")

if __name__ == "__main__":
    run_backtest("AAPL", "1Day", 2000)
