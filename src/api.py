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

matches_table = pd.read_sql(sqlalchemy.text("select * from matches"), engine)

shots_table = pd.read_sql(sqlalchemy.text('select * from shots'), engine)

# Agrupamos todos los disparos por partido
shots_dict = {m_id: group for m_id, group in shots_table.groupby('match_id')}
#Necesario diccionario de los equipos por si en un partido un equipo no tira
matches_dict = {r.match_id: [r.home_team, r.away_team] for r in matches_table.itertuples()}

#localhost/simulation/match_id que es el param de abajo
@app.get("/simulation/{match_id}")
def simulation_endpoint(match_id: int):
    return utils.simulate_match(match_id, engine)

#localhost/standings?simulations=nSimus que es el param de abajo
@app.get("/standings")
def get_standings(simulations: int = 100):

    match_ids = list(shots_dict.keys())

    teams = matches_table['home_team'].unique().tolist()
    base_table = {}
    for team in teams:
        base_table[team] = 0
    


    for simulation in range(simulations):
        for id in match_ids:
            result = utils.simulate_match(shots_dict[id], matches_dict[id])
            points = utils.calculate_points(result)
            for team in list(result.keys()):
                base_table[team] += points[team]
    
    results = [{"team": team, "points": round(total / simulations, 2)}
               for team, total in base_table.items()
]
    
    final_table = sorted(results, key=lambda x: x['points'], reverse=True)

    return final_table


