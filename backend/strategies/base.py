import pandas as pd
from .moving_avg import get_moving_average_signals
from .rsi import get_rsi_signals
from .ema import get_ema_signals
from .rsi_ema import get_rsi_ema_signals

def base_strategy(ohlcv_data: pd.DataFrame, strategy_name: str) -> pd.DataFrame:
    df=ohlcv_data.copy()

    match strategy_name.lower():
        case "moving_average":
            return get_moving_average_signals(df)
        case "rsi":
            return get_rsi_signals(df)
        case "ema":
            return get_ema_signals(df)
        case "rsi_ema":
            return get_rsi_ema_signals(df)
        case _:
            raise ValueError(f"Strategy '{strategy_name}' is not supported.")

    return df