import pandas as pd
from .ema import exponential_moving_avg
from .rsi import relative_strength_index

def get_rsi_ema_signals(ohlcv_data: pd.DataFrame, rsi_period: int = 14, ema_period: int = 9) -> pd.DataFrame:

    df = ohlcv_data.copy()

    df["RSI"] = relative_strength_index(df["Close"], period=rsi_period)
    df["EMA"] = exponential_moving_avg(df["Close"], period=ema_period)

    df["Signal"] = 0

    buy_signal = (df["RSI"] < 50) & (df['Close'] > df["EMA"])
    sell_signal = (df["RSI"] > 50) & (df['Close'] < df["EMA"])

    df.loc[buy_signal, "Signal"] = 1
    df.loc[sell_signal, "Signal"] = -1

    return df