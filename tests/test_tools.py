import json
import pandas as pd
from unittest.mock import patch, MagicMock
from app.tools.finance_tools import get_stock_price

@patch("yfinance.Ticker")
def test_get_stock_price_mocked(mock_ticker):
    mock_data = pd.DataFrame({
        'Close': [150.00]
    }, index=pd.to_datetime(['2026-03-16']))

    mock_instance = MagicMock()
    mock_instance.history.return_value = mock_data
    mock_instance.info = {"previousClose": 140.00}
    mock_ticker.return_value = mock_instance

    result = get_stock_price.invoke({"ticker": "AAPL"})
    
    data = json.loads(result)

    assert data["price"] == "$150.00"
    assert data["ticker"] == "AAPL"
    # (150 - 140) / 140 = 7.1428...
    assert "7.14%" in data["change"]