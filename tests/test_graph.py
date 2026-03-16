from unittest.mock import patch
from langchain_core.messages import AIMessage
from app.graph import graph

# We patch the 'invoke' method of the ChatOpenAI class
# This intercepts the call regardless of where the instance lives
@patch("langchain_openai.ChatOpenAI.invoke") 
def test_full_graph_flow(mock_invoke):

    mock_invoke.return_value = AIMessage(content="Mocked Financial Report")
    
    inputs = {"messages": [("user", "Compare AAPL and MSFT")]}
    config = {"configurable": {"thread_id": "test-123"}}

    output = graph.invoke(inputs, config)

    assert "messages" in output
    assert output["messages"][-1].content == "Mocked Financial Report"
    assert mock_invoke.called