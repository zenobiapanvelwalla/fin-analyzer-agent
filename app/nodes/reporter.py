# app/nodes/reporter.py
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

llm = ChatOpenAI(model="gpt-4o", temperature=0.2) # Low temperature for consistency

def reporter_node(state):
    """
    Synthesizes the research into a formal financial brief.
    """
    # 1. Define the persona and template
    system_prompt = (
        "You are a Senior Equity Research Analyst and investment strategist. Your task is to take the provided "
        "research data and format it into a professional investment brief. "
        "Use the following structure:\n"
        "## Investment Summary\n"
        "## Key Findings\n"
        "## Risk Factors\n"
        "## Sentiment Analysis (-1 to 1)"
        "If you see data for multiple stocks, you MUST create a 'Side-by-Side Comparison' table. "
        "Compare them on: Price, P/E Ratio, Market Cap, and Sentiment. "
        "Finish with a clear recommendation on which stock currently shows better value."
    )
    
    # 2. Extract the research data from messages
    # We grab all messages to ensure the LLM sees the search results
    messages = [SystemMessage(content=system_prompt)] + state["messages"]
    
    # 3. Generate the report
    report = llm.invoke(messages)
    
    # 4. Return the report to be added to the state
    return {"messages": [report]}