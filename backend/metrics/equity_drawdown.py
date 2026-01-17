import pandas as pd

def calculate_equity_drawdown(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['Equity'] = df['PnL'].cumsum()
    df['Peak'] = df['Equity'].cummax()
    df['Drawdown'] = df['Peak'] - df['Equity']
    return df