# Gigi: AI Personal Assistant

Gigi is an AI-powered personal assistant built with Flask, LangChain, and LangGraph. Gigi can help you build your daily schedule, write emails, track progress on goals, and build a budget.

## Project Structure

```
gigi/
├── api/                # Flask backend API
├── ai_engine/          # LangChain/LangGraph logic
│   ├── core.py
│   ├── chains/
│   │   ├── schedule.py
│   │   ├── email.py
│   │   ├── goals.py
│   │   └── budget.py
│   └── utils.py
├── data/               # Database models, migrations
├── integrations/       # Third-party API wrappers
├── ui/                 # Frontend (to be implemented)
├── tests/              # Tests
├── requirements.txt    # Python dependencies
└── README.md
```

## Setup

1. Create a virtual environment and install dependencies:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run the Flask API:
   ```sh
   cd api
   flask run
   ```

## Next Steps
- Implement LangChain/LangGraph logic in each chain module.
- Add integrations for calendar, email, and finance APIs.
- Build a frontend UI.
