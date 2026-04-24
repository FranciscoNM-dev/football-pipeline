from statsbombpy import sb
import pandas as pd


def get_shots(competition_id: int, season_id: int) -> pd.DataFrame:
    """
    Descarga todos los tiros de una temporada y competición.
    Devuelve un DataFrame con un tiro por fila.
    """
    matches = sb.matches(competition_id=competition_id, season_id=season_id)
    match_ids = matches['match_id'].tolist()

    all_shots = []

    for match_id in match_ids:
        events = sb.events(match_id=match_id)
        shots = events[events['type'] == 'Shot']
        shots = shots.copy()
        shots['match_id'] = match_id
        all_shots.append(shots)

    return pd.concat(all_shots, ignore_index=True)

def get_matches(competition_id: int, season_id: int) -> pd.DataFrame:
    matches = sb.matches(competition_id=competition_id, season_id=season_id)


    return matches[['match_id', 'home_team', 'away_team']]