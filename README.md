# Deep Research Agent

Deep Research Agent is an AI-powered research assistant that automates the process of planning, searching, summarizing, reporting, and emailing research on any topic. It leverages LLM agents, web search, and email APIs to deliver detailed, structured research reports.

## Features

- **Automated Research Planning:** Plans multiple web searches for a given query.
- **Web Search & Summarization:** Performs web searches and summarizes results concisely.
- **Report Generation:** Produces a detailed, multi-page markdown report.
- **Email Delivery:** Sends the final report as a well-formatted HTML email.
- **Streamlit UI:** Simple web interface for entering research queries and viewing progress.

## How It Works

1. **User enters a research topic** in the Streamlit web app.
2. The system plans relevant web searches.
3. Each search is performed and summarized.
4. A comprehensive report is generated.
5. The report is emailed to a specified recipient.


## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/deep_research_agent.git
   cd deep_research_agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file with your API keys (e.g., `RESEND_API_KEY` for email).

4. **Run the app locally:**
   ```bash
   streamlit run app.py
   ```

## Deployment

You can deploy this app for free on [Streamlit Cloud](https://streamlit.io/cloud).

**Live App:**  
[https://deep-research-agent-6qcfuqvqrtbtttyvn82cdv.streamlit.app/]

## Requirements

- Python 3.9+
- See `requirements.txt` for all dependencies.

## License

MIT License

---

*Built with ❤️ using Streamlit and OpenAI
