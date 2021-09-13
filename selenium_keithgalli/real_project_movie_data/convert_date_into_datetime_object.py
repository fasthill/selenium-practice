# Convert datas into datetime objects
from module_collection import get_info_box, save_data, load_data, minute_to_integer
from module_datetime_conversion import date_conversion
import json
import re

movie_info_list = load_data('data/disney_datam.json')
dates = [date.get('Release date','N/A') for date in movie_info_list]

date_str = [date_conversion(date) for date in dates]

for movie in movie_info_list:
    date = movie.get('Release date', 'N/A')
    movie['Release date (datetime)'] = date_conversion(date)

print('1')