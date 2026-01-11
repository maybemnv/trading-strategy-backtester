from fastapi import FastAPI
from utils.load_data import load_stock_data

app = FastAPI(title="Trading Strategy Backtester")

@app.get("/")
def health_check():
    return {"status": "Backend running successfully"}

@app.get("/test-data")
def get_stock_data():
    data = load_stock_data("AAPL", "2022-01-01", "2022-03-01")
    return data.head().to_dict(orient="records")

