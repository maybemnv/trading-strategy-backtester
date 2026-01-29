import "./inputForm.css";

function InputForm({
  symbol,
  setSymbol,
  startDate,
  setStartDate,
  endDate,
  setEndDate,
  strategy,
  setStrategy,
  onSubmit,
  loading,
}) {
  const handleSubmit = () => {
    if (!symbol) {
      alert("Please enter a stock symbol");
      return;
    }

    if (startDate > endDate) {
      alert("Start date cannot be after end date");
      return;
    }

    onSubmit();
  };

  return (
    <div className="form-card">
      <div className="form-group">
        <label>Stock Symbol</label>
        <input
          type="text"
          placeholder="e.g. AAPL"
          value={symbol}
          onChange={(e) => setSymbol(e.target.value.toUpperCase())}
        />
      </div>

      <div className="form-group">
        <label>Start Date</label>
        <input
          type="date"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
        />
      </div>

      <div className="form-group">
        <label>End Date</label>
        <input
          type="date"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
        />
      </div>

      <div className="form-group">
        <label>Strategy</label>
        <select value={strategy} onChange={(e) => setStrategy(e.target.value)}>
          <option value="moving_avg">SMA</option>
          <option value="rsi">RSI</option>
          <option value="ema">EMA</option>
          <option value="rsi_ema">RSI + EMA</option>
        </select>
      </div>

      <button
        className="run-btn"
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? "Running Backtest..." : "Run Backtest"}
      </button>
    </div>
  );
}

export default InputForm;
