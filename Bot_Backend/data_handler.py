def add_indicators(df):
    df['MA10'] = df['close'].rolling(window=10).mean()
    df['MA50'] = df['close'].rolling(window=50).mean()
    df['Return'] = df['close'].pct_change()
    df['Target'] = (df['close'].shift(-1) > df['close']).astype(int)
    return df.dropna()
