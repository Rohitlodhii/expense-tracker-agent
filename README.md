# AI Expense Tracker Agent

An intelligent expense tracker powered by Streamlit, PaddleOCR, and LangChain agents.

## Features

- **Document & Receipt Upload**: Supports receipts and invoices in PDF, PNG, JPG, and JPEG formats.
- **Local OCR Extraction**: Uses PaddleOCR to extract text directly from receipts.
- **AI Agent Tool Calling**: Extracts transaction details (date, vendor/service, payment method, amount paid, and running balance) using LangChain agents and automatically logs them into csv/accounts.csv.
- **Live CSV Preview**: Displays and updates transaction history directly in the Streamlit UI.

## Setup

1. **Clone the repository**:
   `ash
   git clone https://github.com/Rohitlodhii/expense-tracker-agent.git
   cd expense-tracker-agent
   `

2. **Set up virtual environment**:
   `ash
   python -m venv .venv
   # On Windows:
   .venv\Scriptsctivate
   # On Linux/macOS:
   source .venv/bin/activate
   pip install -r requirements.txt
   `

3. **Configure environment variables**:
   Create a .env file based on .env.example:
   `dotenv
   OPENAI_API_KEY=your_api_key_here
   OPENAI_BASE_URL=https://integrate.api.nvidia.com/v1
   OPENAI_MODEL=nvidia/nemotron-3.5-super-vl-120b-a12b
   `

4. **Run the application**:
   `ash
   streamlit run app.py
   `
