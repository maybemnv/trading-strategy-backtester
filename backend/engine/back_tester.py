import pandas as pd
from .risk import risk_assessment
# from backend.strategies.base import base_strategy
# from backend.utils.load_data import load_stock_data

def back_tester(ohlcv_data: pd.DataFrame, takeProfit_pct: float = 0.05, stopLoss_pct: float = 0.02) -> pd.DataFrame:
    df=ohlcv_data.copy()

    df['position'] = 0
    df['entry_price'] = 0.0
    df['exit_price'] = 0.0
    df['PnL'] = 0.0
    
    entry_price = 0.0
    stop_loss_price = 0.0
    take_profit_price = 0.0
    in_position = False
    
    for index in range(len(df)-1):

        signal = df.iloc[index]['Signal']

        if in_position:
            df.loc[index+1, 'position'] = 1
        
        if signal == 1 and not in_position:
            entry_price = df.loc[index+1, 'Open']
            stop_loss_price, take_profit_price = risk_assessment(entry_price, takeProfit_pct, stopLoss_pct)
            df.loc[index+1, 'entry_price'] = entry_price 
            in_position = True

        elif in_position:
            low = df.loc[index + 1, "Low"]
            high = df.loc[index + 1, "High"]

            # Stop Loss FIRST
            if low <= stop_loss_price:
                df.loc[index + 1, "exit_price"] = stop_loss_price
                df.loc[index + 1, "PnL"] = stop_loss_price - entry_price
                df.loc[index + 1, "position"] = 0
                in_position = False

            # Take Profit
            elif high >= take_profit_price:
                df.loc[index + 1, "exit_price"] = take_profit_price
                df.loc[index + 1, "PnL"] = take_profit_price - entry_price
                df.loc[index + 1, "position"] = 0
                in_position = False

            # Strategy exit
            elif signal == -1:
                exit_price = df.loc[index + 1, "Close"]
                df.loc[index + 1, "exit_price"] = exit_price
                df.loc[index + 1, "PnL"] = exit_price - entry_price
                df.loc[index + 1, "position"] = 0
                in_position = False

    return df

