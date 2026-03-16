# 📈 FinAnalyzer: Agentic Equity Research Suite
FinAnalyzer is an autonomous AI agent built with **LangGraph** and **GPT-4o**, designed to perform real-time financial research and stock comparisons. Unlike standard chatbots, FinAnalyzer uses a cyclic graph architecture to research data, verify metrics via the Yahoo Finance API, and synthesize professional investment briefs.


## 🚀 Key Features

* **Autonomous Research Loop:** Uses a LangGraph-driven state machine to iteratively search and verify financial data.
* **Parallel Tool Execution:** Capable of researching multiple tickers simultaneously (e.g., comparing NVDA vs. AMD) using parallel tool calling.
* **Real-time Financial Integration:** Fetches live market data, P/E ratios, and company profiles via the yfinance API.
* **Intelligent Reporting:** A dedicated Reporter node synthesizes raw data into structured Markdown reports, including comparison tables and sentiment analysis.
* **Persistent Memory:** Uses MemorySaver to maintain context across multi-turn conversations, allowing users to ask follow-up questions about specific metrics.


## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Orchestration** | [LangGraph](https://langchain-ai.github.io/langgraph/) |
| **LLM** | OpenAI GPT-4o |
| **Data Sources** | yfinance API, Tavily Search |
| **Interface** | Streamlit |
| **Persistence** | LangGraph MemorySaver |


## 🏗️ Architecture

The application operates as a directed acyclic graph (DAG) with a loop for tool execution:
1.  **START**: The user provides a query (e.g., "Compare AAPL and MSFT").
2.  **Researcher Node**: The LLM decides which tools are needed. If multiple stocks are mentioned, it calls tools for all of them.
3.  **ToolNode**: Executes Python functions in parallel to fetch data.
4.  **Reporter Node**: Once all data is gathered, this node synthesizes a final report.
5.  **END**: The final report is streamed to the Streamlit UI.

# 🚦 Getting Started
1. Clone the repository
```bash
git clone https://github.com/zenobiapanvelwalla/finanalyzer-agent.git
cd finanalyzer-agent
```

2. Set up your environment
Create a .env file in the root directory:
```
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
streamlit run main.py
```

# 📊 Example Queries
* "Analyze Tesla (TSLA) and give me a summary of their current valuation."

* "Compare Microsoft (MSFT) and Google (GOOGL). Which one has a better P/E ratio and what is the recent news sentiment?"

* "What are the key financial metrics for NVIDIA right now?"
