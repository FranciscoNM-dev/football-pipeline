# Football Pipeline — La Liga 2016 Simulator

## What it does
This football pipeline allows the user to perform a post-mortem simulation of the whole 2015-2016 LaLiga Season, based on the shots that took place on each game to determine 'how the match should have ended'. Based on the result, points are given to each team and after all simulations have concluded, the ranking can be obtained

## Tech stack
- **Python** — core logic
- **StatsBomb** — to get the raw data
- **PostgreSQL + SQLAlchemy** — data storage and retrieval
- **FastAPI + uvicorn** — API structure to make use of the Data
- **Docker Compose** — orchestrates the PostgreSQL container

## How to run
```bash
git clone https://github.com/FranciscoNM-dev/football-pipeline.git
cd football-pipeline
docker compose up -d
python -m venv .venv
source .venv/Scripts/activate  # Windows
pip install -r requirements.txt
python main.py  # populate the database
uvicorn src.api:app --reload
```

## Endpoints
- `GET /simulation/{match_id}` — returns the expected result for the match based on the shots that took place that day
- `GET /standings?simulations=N` — returns the standings, with the expected amount of points for each of the teams, all of them sorted by this expected amount to get in what position they 'should have ended'

## Project structure
```
football-pipeline/
├── src/
│   ├── api.py        # FastAPI endpoints
│   ├── extract.py    # StatsBomb data extraction
│   ├── load.py       # PostgreSQL data loading
│   ├── transform.py  # Data cleaning and preparation
│   └── utils.py      # Simulation logic
├── data/             # Raw data cache
├── docker-compose.yml
├── main.py           # Pipeline entry point
└── requirements.txt
```
## Next steps
- More uses off the data used in this project. Top scorers, most assists, expected goals vs goals scored...
- Develop a frontend to help UI
