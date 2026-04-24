from src.extract import get_shots, get_matches
from src.load import save_shots, save_matches
from src.transform import clean_shots


save_shots(clean_shots(get_shots(competition_id = 11, season_id = 27)))

save_matches(get_matches(competition_id = 11, season_id = 27))
