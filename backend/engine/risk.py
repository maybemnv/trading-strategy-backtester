import pandas as pd 

def risk_assessment(entry_price: float, takeProfit_pct: float, stopLoss_pct: float):
    
    take_profit_price = entry_price * (1 + takeProfit_pct)
    stop_loss_price = entry_price * (1 - stopLoss_pct)
    
    return take_profit_price, stop_loss_price