import yfinance as yf
from langchain_core.tools import tool
import json

@tool
def get_stock_price(ticker: str) -> str:
    """
    Fetches the current stock price and daily change for a given ticker symbol.
    Use this when the user asks for 'current price', 'quotes', or 'valuation'.
    """
    try:
        stock = yf.Ticker(ticker.upper())
        hist = stock.history(period="1d")
        if hist.empty:
            return f"Error: No data found for ticker {ticker}."
        
        current_price = hist['Close'].iloc[-1]
        prev_close = stock.info.get('previousClose', current_price)
        change_pct = ((current_price - prev_close) / prev_close) * 100
        
        return json.dumps({
            "ticker": ticker.upper(),
            "price": f"${current_price:.2f}",
            "change": f"{change_pct:.2f}%"
        })
    except Exception as e:
        return f"Error fetching price: {str(e)}"

@tool
def get_company_profile(ticker: str) -> str:
    """
    Fetches the company description, industry, and sector.
    Use this when the user asks 'What does this company do?' or for a background check.
    """
    try:
        stock = yf.Ticker(ticker.upper())
        info = stock.info
        profile = {
            "name": info.get("longName"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "summary": info.get("longBusinessSummary")[:500] + "..." # Truncate for efficiency
        }
        return json.dumps(profile)
    except Exception as e:
        return f"Error fetching profile: {str(e)}"

@tool
def get_price_history(ticker: str, period: str = "1mo") -> str:
    """
    Fetches historical stock prices. Period options: '1mo', '3mo', '1y'.
    Use this to identify trends or calculate recent performance.
    """
    try:
        stock = yf.Ticker(ticker.upper())
        hist = stock.history(period=period)
        # We take the closing prices and format them briefly
        prices = hist['Close'].resample('W').last().to_dict() # Weekly closes to save tokens
        return json.dumps({ticker: {str(k.date()): f"${v:.2f}" for k, v in prices.items()}})
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def get_financial_metrics(ticker: str) -> str:
    """
    Fetches key metrics: Market Cap, P/E Ratio, 52-week High/Low.
    Use this for fundamental analysis of a company's value.
    """
    try:
        stock = yf.Ticker(ticker.upper())
        info = stock.info
        metrics = {
            "market_cap": info.get("marketCap"),
            "forward_pe": info.get("forwardPE"),
            "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
            "fifty_two_week_low": info.get("fiftyTwoWeekLow")
        }
        return json.dumps(metrics)
    except Exception as e:
        return f"Error: {str(e)}"