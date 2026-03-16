from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode

from app.nodes.reporter import reporter_node
from .state import AgentState
from .nodes.researcher import researcher_node, tools
from langgraph.checkpoint.memory import MemorySaver

# Define the workflow
builder = StateGraph(AgentState)

# Add Nodes
builder.add_node("researcher", researcher_node)
builder.add_node("tools", ToolNode(tools))
builder.add_node("reporter", reporter_node)

# Definition of routing logic: 
# If the researcher calls a tool, go to "tools". 
# If not (meaning research is finished), go to "reporter".
builder.add_edge(START, "researcher")
builder.add_conditional_edges("researcher", lambda x: "tools" if x["messages"][-1].tool_calls else "reporter")
builder.add_edge("tools", "researcher") # Loop back to research after using a tool
builder.add_edge("reporter", END)       # End the graph after the report is generated

# Add persistence
memory = MemorySaver()

graph = builder.compile(checkpointer=memory)