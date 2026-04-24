import sqlalchemy
import pandas as pd
import random


def simulate_match(match_id: int, engine):

    sql = sqlalchemy.text(
    "SELECT * FROM shots WHERE match_id=:match_id_p"
    )
    df = pd.read_sql(sql, engine, params={"match_id_p": match_id})

    sql = sqlalchemy.text(
    "SELECT home_team, away_team from matches WHERE match_id=:match_id_p"
    )
    teams_df = pd.read_sql(sql, engine, params={"match_id_p": match_id})
    teams = teams_df.iloc[0].tolist()

    score = {item: 0 for item in teams}
    for index, row in df.iterrows():
        if random.random() <= row['xg']:
            score[row['team']] += 1
    return score

def calculate_points(score):
    teams = list(score.keys())
    points = score.copy()
    if score[teams[0]] > score[teams[1]]:
        points[teams[0]] = 3
        points[teams[1]] = 0
    elif score[teams[0]] < score[teams[1]]:
        points[teams[0]] = 0
        points[teams[1]] = 3
    else:
        points[teams[0]] = 1
        points[teams[1]] = 1
    return points