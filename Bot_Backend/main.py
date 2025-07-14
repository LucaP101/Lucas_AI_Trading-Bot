from alpaca_interface import get_price_data
from data_handler import add_indicators
from model_training import train_model

# Step 1: Get price data
df = get_price_data()

# Step 2: Add indicators and prep data
df = add_indicators(df)

# Step 3: Train the AI model
model = train_model(df)

# Step 4: Make a prediction on the most recent data row
latest = df[['MA10', 'MA50', 'Return']].iloc[-1:]
prediction = model.predict(latest)

# Step 5: Print the result
print("🔮 Prediction:", "BUY 📈" if prediction[0] == 1 else "HOLD/SELL 📉")
