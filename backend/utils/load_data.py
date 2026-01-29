import yfinance as yf
import pandas as pd

def load_stock_data(stock_symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    # Normalize dates to YYYY-MM-DD
    try:
        start_date = pd.to_datetime(start_date, dayfirst=True).strftime('%Y-%m-%d')
        end_date = pd.to_datetime(end_date, dayfirst=True).strftime('%Y-%m-%d')
    except Exception:
        pass # Fallback to original string if parsing fails

    data = yf.download(stock_symbol, start=start_date, end=end_date)

    if data.empty:
        raise ValueError(f"No data found for {stock_symbol} between {start_date} and {end_date}")
    
    # Flatten MultiIndex columns if present (yfinance returns MultiIndex for single stocks)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns]
    
    stock_data = data.reset_index()
    
    # Convert Timestamp to string for JSON serialization
    if 'Date' in stock_data.columns:
        stock_data['Date'] = stock_data['Date'].dt.strftime('%Y-%m-%d')
    
    return stock_data