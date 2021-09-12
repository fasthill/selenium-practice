# Task #3 Clean our data!
from bs4 import BeautifulSoup as bs
import requests
from module_collection import get_info_box, save_data, load_data, minute_to_integer
from module_money_conversion import money_conversion
import json
import re

# Subtasks
# - convert  dates into datetime object
# - convert budget & box office to numbers

# - convert budget & box office to numbers
movie_info_list = load_data('data/disney_datat.json') # after modification time notation

'''
TODO
Given either a string or a list of strings as input, return
a number (int or float) which is equal to the monetary value
money_conversion("$12.2 million") --> 12200000
money_conversion("$790,000") --> 790000
use test_money_conversion.py to test your solution
'''

''' use from module_money_conversion.py
def money_conversion(money):
    pass
'''

''' use test_money_conversion.py to test cases
$30.9 million est. ₹ 79.43 crore (US$11 million)  ₹ 83 crore ['est.', '₹2,024–2,100 crore', '(', '$311–340\xa0million', ')']
$7.7
 million
'''

for mv in movie_info_list:
    money_budget = mv.get('Budget', 'N/A')
    money_box_office = mv.get('Box office', 'N/A')
    mv['Budget (convert)'] = money_conversion(money_budget)
    mv['Box office (convert)'] = money_conversion(money_box_office)

t1 = 'Beauty and the Beast'
aa = [i for i, sub in enumerate(movie_info_list) if sub['title'] == t1]
print (aa)

save_data('data/disney_datam.json', movie_info_list)
