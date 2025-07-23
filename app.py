import streamlit as st
import asyncio
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)

# Async function to stream chunks into a placeholder
async def stream_response(query: str, placeholder):
    output = ""
    async for chunk in ResearchManager().run(query):
        output += chunk
        placeholder.markdown(output, unsafe_allow_html=True)
        await asyncio.sleep(0.01)  # slight delay for smoother updates

# Function to run the async task
def run_streamlit_query(query: str, placeholder):
    asyncio.run(stream_response(query, placeholder))

# Streamlit UI layout
st.set_page_config(page_title="Deep Research", layout="centered")
st.title("🔍 Deep Research")

query = st.text_input("What topic would you like to research?")
submit = st.button("Run")

# Placeholder for streaming output
output_placeholder = st.empty()

if query and submit:
    with st.spinner("Researching..."):
        output_placeholder.empty()  # Clear any previous output
        run_streamlit_query(query, output_placeholder)
