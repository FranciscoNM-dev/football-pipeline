from src import utils
from fastapi import FastAPI
import pandas as pd
import sqlalchemy
from dotenv import load_dotenv #needed for postgresql connection
import os #needed fot postgresql connection


app = FastAPI()

load_dotenv()
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
name = os.getenv('DB_NAME')
engine = sqlalchemy.create_engine(f"postgresql://{user}:{password}@{host}:{port}/{name}")

#localhost/simulation/match_id que es el param de abajo
@app.get("/simulation/{match_id}")
def simulation_endpoint(match_id: int):
    return utils.simulate_match(match_id, engine)

#localhost/standings?simulations que es el param de abajo
@app.get("/standings")
def get_standings(simulations: int = 100):
    sql = sqlalchemy.text(
    "SELECT distinct match_id FROM shots"
    )
    match_ids = pd.read_sql(sql, engine)['match_id'].tolist()

    sql = sqlalchemy.text(
    "SELECT distinct home_team FROM matches"
    )
    teams = pd.read_sql(sql, engine)['home_team'].tolist()
    base_table = {'team': teams, 'points': [0] * len(teams)}
    standings = pd.DataFrame(base_table)

    for simulation in range(simulations):
        for id in match_ids:
            result = utils.simulate_match(id, engine)
            points = utils.calculate_points(result)
            for team in list(result.keys()):
                standings.loc[standings.team == team, 'points'] += points[team]
    

    standings['points'] = standings['points'].apply(lambda x: x / simulations)
    final_table = standings.sort_values(by = 'points', ascending = False)
    return final_table.to_dict(orient='records')


