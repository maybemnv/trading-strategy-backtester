import pandas as pd

def exponential_moving_avg(prices: pd.Series, period: int) -> pd.Series:
    return prices.ewm(span=period, adjust=False).mean()

def get_ema_signals(ohlcv_data: pd.DataFrame, short_period: int = 12, long_period: int = 26) -> pd.DataFrame:

    df = ohlcv_data.copy()

    df["EMA_Short"] = exponential_moving_avg(df["Close"], short_period)
    df["EMA_Long"] = exponential_moving_avg(df["Close"], long_period)

    df["Signal"] = 0

    buy_signal = (
        (df["EMA_Short"] > df["EMA_Long"]) &
        (df["EMA_Short"].shift(1) <= df["EMA_Long"].shift(1))
    )

    sell_signal = (
        (df["EMA_Short"] < df["EMA_Long"]) &
        (df["EMA_Short"].shift(1) >= df["EMA_Long"].shift(1))
    )

    df.loc[buy_signal, "Signal"] = 1
    df.loc[sell_signal, "Signal"] = -1

    return df
