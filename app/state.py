from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    # Annotating with add_messages ensures new tool outputs append to history
    messages: Annotated[list[BaseMessage], add_messages]
    stock_ticker: str