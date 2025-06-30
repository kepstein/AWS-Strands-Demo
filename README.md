# Stocks Analyst AI Agent

An AI-powered financial analyst that provides comprehensive stock analysis using real-time data and advanced charting.

## Features

- **Automated Stock Analysis**: Analyzes any stock symbol with detailed financial metrics
- **Visual Charts**: Generates 20-day moving averages and daily return comparisons against S&P 500
- **Risk Assessment**: Calculates volatility and other key financial indicators
- **AI-Powered Insights**: Uses Claude 3.5 Sonnet for intelligent analysis and recommendations
- **Observability**: Integrated with LangFuse for tracking and analytics

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up LangFuse tracking** (optional):
   ```bash
   cp .env.example .env
   # Edit .env with your LangFuse credentials
   ```

3. **Run analysis**:
   ```bash
   python stocks_analyst.py
   ```

## How It Works

The agent uses the Strands framework to orchestrate:
- **Data Collection**: Fetches historical stock data via `yfinance`
- **Analysis**: Performs technical analysis and risk calculations
- **Visualization**: Creates interactive charts and graphs
- **Reporting**: Generates comprehensive analysis reports

## Built With

- [AWS Strands](https://github.com/aws-samples/strands) - AI agent framework
- [Claude 3.5 Sonnet](https://anthropic.com) - Large language model
- [LangFuse](https://langfuse.com) - Observability and analytics
- [yfinance](https://pypi.org/project/yfinance/) - Stock data API



