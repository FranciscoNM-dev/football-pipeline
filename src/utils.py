import sqlalchemy
import pandas as pd
import random


def simulate_match(shots_dict, teams):

    score = {team: 0 for team in teams}
    
    for row in shots_dict.itertuples():
        if random.random() <= row.xg:
            score[row.team] += 1
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