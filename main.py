import streamlit as st
from dotenv import load_dotenv

# Load the .env file before importing your custom modules
load_dotenv()

import uuid
from app.graph import graph
from langchain_core.messages import HumanMessage, AIMessage

# --- 1. Page Configuration
st.set_page_config(page_title="FinAnalyzer Pro", page_icon="📈", layout="wide")
st.title("📈 FinAnalyzer: Advanced Research Agent")
st.markdown("Analyze stocks using real-time web search and financial metrics")

# --- 2. Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

# --- 3. Display Chat History
for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)


# --- 4. Chat Input
if prompt := st.chat_input("What stock should I analyze today?"):
    # User Message
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # --- 5. Graph Execution ---
    with st.chat_message("assistant"):
        # The 'expanded=False' keeps the internal logs hidden by default
        with st.status("🔍 Analyzing market data and financial news...", expanded=False) as status:
            config = {"configurable": {"thread_id": st.session_state.thread_id}}
            
            try:
                # We run the stream to let the graph work, 
                for _ in graph.stream({"messages": st.session_state.messages}, config, stream_mode="updates"):
                    pass # Just let the graph process silently
                
                status.update(label="✅ Research finalized. Generating report...", state="complete", expanded=False)
                
                # Pull final result
                final_state = graph.get_state(config)
                final_report = final_state.values["messages"][-1].content
                
                status.update(label="📃 Report Generated", state="complete", expanded=True)

                st.markdown(final_report)
                st.session_state.messages.append(AIMessage(content=final_report))

            except Exception as e:
                # Catch technical errors and show a friendly message
                status.update(label="⚠️ Research Interrupted", state="error", expanded=False)
                error_msg = "I encountered an issue gathering the latest data. Please try again or check the ticker symbol."
                st.info(error_msg)
                # Log the real error to your console for debugging
                print(f"Error: {e}")
