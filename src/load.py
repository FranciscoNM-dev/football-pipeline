from sqlalchemy import create_engine
import pandas as pd
import os #para las credenciales de la BD
from dotenv import load_dotenv
load_dotenv()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
name = os.getenv('DB_NAME')
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{name}") #Crea la conexión pero aún no conecta

def save_shots(clean_df: pd.DataFrame):

    clean_df.to_sql('shots', engine, if_exists='replace', index=False) #Aquí sí conecta y manda esos datos


def save_matches(matches_df: pd.DataFrame):
    matches_df.to_sql('matches', engine, if_exists='replace', index=False)