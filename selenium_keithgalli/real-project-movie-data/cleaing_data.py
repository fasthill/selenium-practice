# Task #3 Clean our data!
from bs4 import BeautifulSoup as bs
import requests
from module_collection import get_info_box, save_data, load_data, minute_to_integer
import json

# Subtasks
# - clean up references [1]
# - Convert running time into an integer
# - convert  dates into datetime object
# - split up the long strings
# - convert budget & box office to numbers

# # cleaning up references (remove [1] [2] etc), undisplayed contents (display:none)
# below is test data movie
# movie_info = get_info_box('https://en.wikipedia.org/wiki/Peter_Pan_(1953_film)')
# # change the module_collection: clean_tag()
#
# # split up the long strings
# below are test data movies
# movie_info = get_info_box('https://en.wikipedia.org/wiki/The_Great_Locomotive_Chase') # make long string into list separated by 'br'
#
# movie_info = get_info_box('https://en.wikipedia.org/wiki/Davy_Crockett:_King_of_the_Wild_Frontier_(film)')  # same as above
#

#convert running time into an integer
# movie_info_list에서 minutes가 어떻게 표현되고 있는지 확인하는 과정
movie_info_list = load_data('data/disney_data.json')
movie_info_list_temp = []
for movie in movie_info_list:
    print(movie.get('Running time', 'N/A'))  # 'Running time" key가 없을 때 'N/A'반환. 모든 key가 일정치 않아서 확인하는 과정
# 상기 과정을 거쳐 데이터를 확인하고 하나 하나 데이터 정리함
    movie['Running time (int)'] = minute_to_integer(movie.get('Running time', 'N/A'))
    movie_info_list_temp.append(movie)

save_data('data/disney_datat.json', movie_info_list_temp)

# movie_info = get_info_box('https://en.wikipedia.org/wiki/Zorro_(1957_TV_series)#Theatrical')  # correct Nonetype error no attribute 'find'
