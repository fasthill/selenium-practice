
from module_collection import save_data_pickle, load_data_pickle
from module_get_rating_from_db_api import get_rating_db

movie_info_list = load_data_pickle('data/disney_data_score_api.pkl')

# movie_info_list_temp = []
for i, movie in enumerate(movie_info_list):
    ri = movie.get('Rating (imdb)','N/A')
    vr = movie.get('Value (rotten_tomatoes)','N/A')
    if ri == 'N/A' and vr == 'N/A':
        print("NUM ", i, "title", movie.get('title', 'N/A'), ri, vr)
#
print("1")
# save_data_pickle('data/disney_data_score_api.pkl', movie_info_list_temp)
