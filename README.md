
# AnalitycsP2P

AI Copilot for P2P crypto trading and arbitrage analysis.

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and fill in your values
3. Install dependencies: `pip install -r requirements.txt`
4. Run the server: `python main.py`

## Environment Variables

- `PROJECT_NAME`: Name of the project
- `OPENAI_API_KEY`: Your OpenAI API key
- `PORT`: Server port (default: 5000)

## API Endpoints

- `GET /`: Health check
- `GET /check-env`: Verify environment setup
- `POST /ia`: Execute AI agent with prompt
