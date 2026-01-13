import pandas as pd
from moving_avg import moving_avg

def base_strategy(ohlcv_data: pd.DataFrame, strategy_name: str) -> pd.DataFrame:

    if strategy_name != "moving_average":
        raise ValueError(f"Strategy '{strategy_name}' is not recognized.")

    short_window = 20
    long_window = 50

    close_prices = ohlcv_data["Close"]

    ohlcv_data["SMA_Short"] = moving_avg(close_prices, short_window)
    ohlcv_data["SMA_Long"] = moving_avg(close_prices, long_window)

    ohlcv_data["Signal"] = 0

    buy_signal = (
        (ohlcv_data["SMA_Short"] > ohlcv_data["SMA_Long"]) &
        (ohlcv_data["SMA_Short"].shift(1) <= ohlcv_data["SMA_Long"].shift(1))
    )

    sell_signal = (
        (ohlcv_data["SMA_Short"] < ohlcv_data["SMA_Long"]) &
        (ohlcv_data["SMA_Short"].shift(1) >= ohlcv_data["SMA_Long"].shift(1))
    )

    ohlcv_data.loc[buy_signal, "Signal"] = 1
    ohlcv_data.loc[sell_signal, "Signal"] = -1

    return ohlcv_data
