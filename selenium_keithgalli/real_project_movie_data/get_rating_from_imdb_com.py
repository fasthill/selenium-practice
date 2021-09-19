# Task 4 attach IMDB/Rotten Tomato Scores
from module_collection import  load_data, save_data_pickle, load_data_pickle
from module_get_rating_from_imdb import get_movie_rating_imdb
from module_datetime_conversion import date_conversion
import pickle
import json
import re

movie_info_list = load_data_pickle('data/disney_datad.pkl')
# use dombo 1941.

#get_movie_rating_imdb()
# for movie in movie_info_list:
movie_info_list_temp = []
for movie in movie_info_list[14:15]:
    title = movie.get('title', 'N/A')
    if title == 'N/A':
        continue  #
    date = movie.get('Release date (datetime)', 'N/A')
    if date == 'N/A':
        continue  #
    year = date.strftime('%Y')
    score, base = get_movie_rating_imdb(title, year)
    print("IN Main", score, base)
    movie['Rating'] = score
    movie_info_list_temp.append(movie)

save_data_pickle('data/disney_data_score.pkl', movie_info_list_temp)
# save_data('data/disney_datad.json', movie_info_list_temp)  # can't write datetime object into json.
