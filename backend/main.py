from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from utils.load_data import load_stock_data
from strategies.base import base_strategy
from engine.back_tester import back_tester
from metrics.metrics import calculate_metrics
from metrics.equity_drawdown import calculate_equity_drawdown

app = FastAPI(
    title="Trading Strategy Backtester",
    description="A Python-based trading strategy backtesting API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BacktestRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str
    strategy: str


@app.get("/")
def health_check():
    return {"status": "Backend running successfully"}

@app.post("/api/v1/backtest")
def run_backtest(request: BacktestRequest):
    try:
        ohlcv_data = load_stock_data(request.symbol.upper(), request.start_date, request.end_date)
        strategy_data = base_strategy(ohlcv_data, request.strategy)
        backtested_data = back_tester(strategy_data)
        df = calculate_equity_drawdown(backtested_data)
        metrics = calculate_metrics(df)

        return {
           "symbol": request.symbol.upper(),
            "strategy": request.strategy,
            "metrics": metrics.to_dict(orient="records"),
            "equity_data": df[["Date", "Equity", "Drawdown"]].to_dict(orient="records")
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
