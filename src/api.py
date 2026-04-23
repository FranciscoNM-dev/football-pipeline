from fastapi import FastAPI
import random
import pandas as pd
import sqlalchemy
from dotenv import load_dotenv #needed for postgresql connection
import os #needed fot postgresql connection

load_dotenv()

app = FastAPI()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
name = os.getenv('DB_NAME')
engine = sqlalchemy.create_engine(f"postgresql://{user}:{password}@{host}:{port}/{name}")

@app.get("/simulation/{match_id}")
def simulate_match(match_id: int):

    sql = sqlalchemy.text(
    "SELECT * FROM shots WHERE match_id=:match_id_p"
    )
    df = pd.read_sql(sql, engine, params={"match_id_p": match_id})
    score = {item: 0 for item in df["team"].unique()}
    for index, row in df.iterrows():
        if random.random() <= row['xg']:
            score[row['team']] += 1
    return score

