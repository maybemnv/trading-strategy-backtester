from utils.load_data import load_stock_data
from strategies.base import base_strategy
from engine.back_tester import back_tester
from metrics.metrics import calculate_metrics

# 1️⃣ Load data
df = load_stock_data("AAPL", "2022-01-01", "2022-12-01")

# 2️⃣ Generate signals
df = base_strategy(df, "ema")  # or rsi / moving_average

# 3️⃣ Backtest
df = back_tester(df, 0.04, 0.04)

# 4️⃣ Metrics
metrics = calculate_metrics(df)

print(metrics)
