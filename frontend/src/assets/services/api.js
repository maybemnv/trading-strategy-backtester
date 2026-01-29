import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

export const fetchBacktestResults = async (payload) => {
  try {
    const response = await axios.post(
      `${API_BASE_URL}/api/v1/backtest`,
      payload
    );
    return response.data;
  } catch (error) {
    console.error("API Error:", error);
    throw new Error("Failed to fetch backtest results");
  }
};
