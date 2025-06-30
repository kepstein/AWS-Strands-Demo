# LangFuse Setup Instructions

## Quick Start

1. **Copy the environment file:**
   ```bash
   cp .env.example .env
   ```

2. **Get your LangFuse credentials:**
   - Visit https://cloud.langfuse.com
   - Create a project (or use existing)
   - Go to Settings → API Keys
   - Copy your Public Key and Secret Key

3. **Update your .env file:**
   ```bash
   LANGFUSE_PUBLIC_KEY=pk-lf-your-actual-public-key-here
   LANGFUSE_SECRET_KEY=sk-lf-your-actual-secret-key-here
   LANGFUSE_HOST=https://cloud.langfuse.com
   ```

4. **Run your analysis:**
   ```bash
   python stocks_analyst.py
   ```

5. **View your traces:**
   - Go back to https://cloud.langfuse.com
   - Navigate to your project
   - Check the "Traces" section to see your stock analysis runs

## What's being tracked?

The `@observe` decorator automatically captures:
- Function inputs (stock name)
- Function outputs (analysis results)
- Execution time
- Any errors that occur
- Model usage (if applicable)

All of this appears in your LangFuse dashboard with zero additional code!
