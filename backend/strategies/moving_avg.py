import pandas as pd

def moving_avg(close_data: pd.DataFrame, window_size: int = 20) -> pd.DataFrame:
    
    if close_data is None or close_data.empty:
        raise ValueError("Input DataFrame is empty or None.")
    
    return close_data.rolling(window=window_size).mean()