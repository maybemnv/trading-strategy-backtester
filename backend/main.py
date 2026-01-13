from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from utils.load_data import load_stock_data

app = FastAPI(
    title="Trading Strategy Backtester",
    description="A Python-based trading strategy backtesting API",
    version="0.1.0"
)

# Add CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    """Health check endpoint to verify the API is running."""
    return {"status": "Backend running successfully", "version": "0.1.0"}


@app.get("/api/v1/stock-data")
def get_stock_data(
    symbol: str = Query(..., description="Stock ticker symbol (e.g., AAPL, GOOGL)"),
    start_date: str = Query(..., description="Start date in YYYY-MM-DD format"),
    end_date: str = Query(..., description="End date in YYYY-MM-DD format"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return")
):
    """
    Fetch historical stock data for a given symbol and date range.
    """
    try:
        data = load_stock_data(symbol.upper(), start_date, end_date)
        records = data.head(limit).to_dict(orient="records")
        return {
            "symbol": symbol.upper(),
            "start_date": start_date,
            "end_date": end_date,
            "count": len(records),
            "data": records
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")
