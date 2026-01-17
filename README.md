# 📈 Trading Strategy Backtester (Full Stack)

A **full-stack trading strategy backtesting application** that allows users to test algorithmic trading strategies on historical stock market data and visualize performance metrics through an interactive dashboard.

Built with **FastAPI (backend)** and **React + Vite (frontend)**, this project demonstrates practical knowledge of **quantitative trading logic, data analysis, API design, and frontend visualization**.

---

## 🚀 Features

- 📊 Fetches real historical stock data using Yahoo Finance
- 🧠 Implements multiple trading strategies:
  - Moving Average Crossover
  - RSI (Relative Strength Index)
  - EMA (Exponential Moving Average)
  - RSI + EMA Combined Strategy
- ⚙️ Custom backtesting engine to simulate trades
- 📉 Performance metrics calculation:
  - Total Trades
  - Winning & Losing Trades
  - Win Rate
  - Final Equity
  - Maximum Drawdown
- 📈 Interactive equity curve visualization
- 🎯 User-driven inputs:
  - Stock symbol
  - Date range
  - Strategy selection
- 🌐 Fully integrated REST API + frontend dashboard

---

## 🧱 Tech Stack

### Backend
- **Python**
- **FastAPI**
- **Pandas**
- **yFinance**
- Custom backtesting engine
- Modular strategy architecture

### Frontend
- **React**
- **Vite**
- **TypeScript**
- **Axios**
- **Recharts** (for data visualization)
- Basic custom CSS styling

## 🔁 How It Works

1. User enters stock symbol, date range, and strategy in the frontend
2. Frontend sends request to FastAPI backend
3. Backend:
   - Fetches historical OHLCV data
   - Applies selected trading strategy
   - Simulates trades using a backtesting engine
   - Calculates performance metrics
4. Results are returned to frontend
5. Frontend displays metrics and equity curve graph

---

## ▶️ Running the Project Locally

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
