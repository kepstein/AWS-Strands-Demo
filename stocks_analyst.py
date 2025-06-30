#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from strands_tools import python_repl
from strands import Agent
from langfuse import observe

# Load environment variables from .env file
load_dotenv()

os.environ["BYPASS_TOOL_CONSENT"] = "true"

from langfuse import Langfuse

langfuse = Langfuse(
  secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
  public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
  host=os.getenv("LANGFUSE_HOST")
)

system_prompt = """
You are a financial analyst. You will do the research requested, and create a PDF report. 

- Plot 20-day moving average of Closing prices for the past 1 year
- Plot daily rate of return comparison against the S&P500 for the same period
- Calculate the following metrics:
	- Volatility
	- Volatility for S&P500
	- YTD return
	- S&P500 YTD Return

You should generate a PDF report. The report should be titled '<ticker> Analysis'
The 2 charts should be shown next, and finally a table with the metrics at the bottom. 

When you are done creating the report, delete the temporary files.

Use 'yfinance' to retrieve the historical data and use 'reportlab' to generate the PDF report. 
"""

@observe(name="stock_analysis")
def analyze_stock(stock_name):
    """Analyze a stock with financial metrics and charts"""
    agent = Agent(tools=[python_repl],
            system_prompt=system_prompt,
            model="us.anthropic.claude-3-5-sonnet-20241022-v2:0")

    return agent(stock_name)

# Run the analysis
response = analyze_stock("Amazon")
print(response)
