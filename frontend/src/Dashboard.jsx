import { useState } from "react";
import { fetchBacktestResults } from "./assets/services/api";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";
import InputForm from "./components/inputForm";
import "./Dashboard.css";

function Dashboard() {
  const [symbol, setSymbol] = useState("AAPL");
  const [startDate, setStartDate] = useState("2023-01-01");
  const [endDate, setEndDate] = useState("2023-11-30");
  const [strategy, setStrategy] = useState("rsi");

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const runBacktest = async () => {
    setLoading(true);
    setError("");
    setData(null);

    try {
      const result = await fetchBacktestResults({
        symbol,
        start_date: startDate,
        end_date: endDate,
        strategy,
      });
      setData(result);
    } catch (err) {
      setError("Failed to fetch backtest data");
    } finally {
      setLoading(false);
    }
  };

  const metrics = data?.metrics?.[0];
  const equityData = data?.equity_data;

  return (
    <div className="dashboard">
      <h1 className="title">📈 Trading Strategy Backtester</h1>

      <InputForm
        symbol={symbol}
        setSymbol={setSymbol}
        startDate={startDate}
        setStartDate={setStartDate}
        endDate={endDate}
        setEndDate={setEndDate}
        strategy={strategy}
        setStrategy={setStrategy}
        onSubmit={runBacktest}
        loading={loading}
      />

      {loading && <p className="status">Running backtest...</p>}
      {error && <p className="error">{error}</p>}

      {metrics && equityData?.length > 0 && (
        <>
          <div className="metrics-grid">
            <div className="card">Total Trades: <b>{metrics["Total Trades"]}</b></div>
            <div className="card">Winning Trades: <b>{metrics["Winning Trades"]}</b></div>
            <div className="card">Losing Trades: <b>{metrics["Losing Trades"]}</b></div>
            <div className="card">Win Rate: <b>{metrics["Win Rate (%)"]}%</b></div>
            <div className="card">Final Equity: <b>{metrics["Final Equity"].toFixed(2)}</b></div>
            <div className="card">Max Drawdown: <b>{metrics["Max Drawdown"].toFixed(2)}</b></div>
          </div>

          <h2 className="subtitle">Equity Curve</h2>

          <ResponsiveContainer width="100%" height={350}>
            <LineChart data={equityData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="Date" />
              <YAxis />
              <Tooltip />
              <Line
                type="monotone"
                dataKey="Equity"
                stroke="#2563eb"
                strokeWidth={2}
              />
            </LineChart>
          </ResponsiveContainer>
        </>
      )}
    </div>
  );
}

export default Dashboard;
