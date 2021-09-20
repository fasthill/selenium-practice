
from module_collection import save_data, load_data_pickle
import pandas as pd
from module_get_rating_from_db_api import get_rating_db

movie_info_list = load_data_pickle('data/disney_data_score_api.pkl')

# copy movie data
movie_info_copy = [movie.copy() for movie in movie_info_list]

# convert datetime to string
for movie in movie_info_copy:
    current_date = movie['Release date (datetime)']
    if current_date:
        movie['Release date (datetime)'] = current_date.strftime('%B %d, %Y')
    else:
        movie['Release date (datetime)'] = None

# Now, we can save data to .json and .csv cause there is no datetime type.
save_data('data/disney_data_final.json', movie_info_copy)

df = pd.DataFrame(movie_info_copy)
df.to_csv('data/disney_data_final.csv', index=False)
