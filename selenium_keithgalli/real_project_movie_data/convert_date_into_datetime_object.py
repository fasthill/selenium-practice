# Convert data into datetime objects
from module_collection import  load_data, save_data_pickle
from module_datetime_conversion import date_conversion
import pickle
import json
import re

movie_info_list = load_data('data/disney_datam.json')
# dates = [date.get('Release date','N/A') for date in movie_info_list]
# date_str = [date_conversion(date) for date in dates]

# for movie in movie_info_list:
movie_info_list_temp = []
for movie in movie_info_list:
    date = movie.get('Release date', 'N/A')
    movie['Release date (datetime)'] = date_conversion(date)
    movie_info_list_temp.append(movie)

save_data_pickle('data/disney_datad.pkl', movie_info_list_temp)
# save_data('data/disney_datad.json', movie_info_list_temp)  # can't write datetime object into json.
