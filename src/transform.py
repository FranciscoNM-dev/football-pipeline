import pandas as pd


def clean_shots(ugly_df:pd.DataFrame) -> pd.DataFrame:
    ugly_df = ugly_df.rename(columns={"shot_statsbomb_xg": "xg"})
    ugly_df = ugly_df.dropna(subset=['xg'])
    return ugly_df[['match_id', 'player', 'team', 'minute', 'xg', 'shot_outcome']]

