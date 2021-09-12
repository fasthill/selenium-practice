# Convert datas into datetime objects
from module_collection import get_info_box, save_data, load_data, minute_to_integer
import json
import re

movie_info_list = load_data('data/disney_datam.json')
aa = [date.get('Release date','N/A') for date in movie_info_list]

print(aa)