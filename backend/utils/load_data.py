import yfinance as yf
import pandas as pd

def load_stock_data(stock_symbol : str, start_date : str, end_date : str) -> pd.DataFrame:

    data = yf.download(stock_symbol, start=start_date, end=end_date)

    if data.empty:
        raise ValueError(f"No data found for {stock_symbol} between {start_date} and {end_date}")
    
    stock_data = data.reset_index()
    return stock_data

print(load_stock_data("AAPL", "2022-01-01", "2022-03-01"))
