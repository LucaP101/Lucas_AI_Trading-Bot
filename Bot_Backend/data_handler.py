def add_indicators(df):
    delta = df['close'].diff()  # Calculate the difference in closing prices
    df['MA10'] = df['close'].rolling(window=10).mean()
    df['MA50'] = df['close'].rolling(window=50).mean()
    df['Return'] = df['close'].pct_change()
    df['Target'] = (df['close'].shift(-1) > df['close']).astype(int)
    # RSI indicator now
    gain = delta.clip(lower=0)  # takes gains and clips losses to zero
    loss = -delta.clip(upper=0)  # takes losses and clips gains to zero
    # so we have 2 separate columns one for gains one for losses 
    avg_gain = gain.rolling(window=14).mean()  # takes the mean of 14 days in gains 
    avg_loss = loss.rolling(window=14).mean()  # takes the mean of 14 days in losses
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))


    return df.dropna()
