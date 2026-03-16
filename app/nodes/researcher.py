from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import SystemMessage
# Tools imports
from app.tools.finance_tools import (
    get_stock_price, 
    get_company_profile, 
    get_price_history, 
    get_financial_metrics
)

llm = ChatOpenAI(model="gpt-4o", temperature=0)
search_tool = TavilySearchResults(k=3)
tools = [
    search_tool, 
    get_stock_price, 
    get_company_profile, 
    get_price_history, 
    get_financial_metrics
]

def researcher_node(state):
    # 1. Instruct the LLM to search for everything at once
    system_instruction = SystemMessage(content=(
        "You are an expert financial researcher. "
        "If the user asks to compare multiple items or needs multiple pieces of information, "
        "generate ALL necessary tool calls at once to perform searches in parallel."
    ))

    # 2. Bind the tools (parallel_tool_calls=True is default for GPT-4o, but we can be explicit)
    llm_with_tools = llm.bind_tools(tools)

    # 3. Combine system prompt with existing message history
    messages = [system_instruction] + state["messages"]

    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}