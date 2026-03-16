# 📈 FinAnalyzer: Agentic Equity Research Suite
FinAnalyzer is an autonomous AI agent built with LangGraph and GPT-4o, designed to perform real-time financial research and stock comparisons. Unlike standard chatbots, FinAnalyzer uses a cyclic graph architecture to research data, verify metrics via the Yahoo Finance API, and synthesize professional investment briefs.

# 🚀 Key Features
Autonomous Research Loop: Uses a LangGraph-driven state machine to iteratively search and verify financial data.

Parallel Tool Execution: Capable of researching multiple tickers simultaneously (e.g., comparing NVDA vs. AMD) using parallel tool calling.

Real-time Financial Integration: Fetches live market data, P/E ratios, and company profiles via the yfinance API.

Intelligent Reporting: A dedicated Reporter node synthesizes raw data into structured Markdown reports, including comparison tables and sentiment analysis.

Persistent Memory: Uses MemorySaver to maintain context across multi-turn conversations, allowing users to ask follow-up questions about specific metrics.

# 🛠️ Tech Stack
Framework: LangGraph (Stateful Orchestration)

LLM: OpenAI GPT-4o

UI: Streamlit

Data Sources: Yahoo Finance (yfinance), Tavily Search API

Environment: Python 3.10+

# 🏗️ Architecture
The application follows a modular node-based architecture:

Researcher Node: Interprets user intent and determines which financial tools to call.

ToolNode: Executes Python-based tools in parallel to fetch live market data.

Reporter Node: Aggregates the tool outputs and formats them into a professional investment report.

# 🚦 Getting Started
1. Clone the repository

git clone https://github.com/yourusername/finanalyzer-agent.git
cd finanalyzer-agent

2. Set up your environment
Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key

3. Install dependencies

pip install -r requirements.txt

4. Run the application

streamlit run main.py

# 📊 Example Queries
"Analyze Tesla (TSLA) and give me a summary of their current valuation."

"Compare Microsoft (MSFT) and Google (GOOGL). Which one has a better P/E ratio and what is the recent news sentiment?"

"What are the key financial metrics for NVIDIA right now?"
