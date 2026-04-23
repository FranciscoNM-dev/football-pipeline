from src.extract import get_shots
from src.load import save_shots
from src.transform import clean_shots


save_shots(clean_shots(get_shots(competition_id = 11, season_id = 27)))
