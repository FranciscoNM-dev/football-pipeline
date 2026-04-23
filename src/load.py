from sqlalchemy import create_engine
import pandas as pd
import os #para las credenciales de la BD
from dotenv import load_dotenv
load_dotenv()

def save_shots(clean_df: pd.DataFrame):
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    name = os.getenv('DB_NAME')
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{name}") #Crea la conexión pero aún no conecta
    clean_df.to_sql('shots', engine, if_exists='replace', index=False) #Aquí sí conecta y manda esos datos