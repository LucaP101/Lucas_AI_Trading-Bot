print("🟢 Starting Luca's AI Trading Bot...")

try:
    from alpaca_interface import get_price_data
    print("✅ Imported alpaca_interface")
except Exception as e:
    print("❌ Failed to import alpaca_interface:", e)

try:
    from data_handler import add_indicators
    print("✅ Imported data_handler")
except Exception as e:
    print("❌ Failed to import data_handler:", e)

try:
    from model_training import train_model
    print("✅ Imported model_training")
except Exception as e:
    print("❌ Failed to import model_training:", e)

print("📥 Getting price data from Alpaca...")
try:
    df = get_price_data()
    print("✅ Price data received.")
except Exception as e:
    print("❌ Error getting price data:", e)
    exit()

print("📊 Adding indicators...")
try:
    df = add_indicators(df)
    print("✅ Indicators added.")
except Exception as e:
    print("❌ Error adding indicators:", e)
    exit()

print("🧠 Training model...")
try:
    model = train_model(df)
    print("✅ Model trained.")
except Exception as e:
    print("❌ Error training model:", e)
    exit()

print("🔮 Making prediction...")
try:
    latest = df[['MA10', 'MA50', 'Return']].iloc[-1:]
    prediction = model.predict(latest)
    result = "BUY 📈" if prediction[0] == 1 else "HOLD/SELL 📉"
    print("📈 Prediction:", result)
except Exception as e:
    print("❌ Error making prediction:", e)
