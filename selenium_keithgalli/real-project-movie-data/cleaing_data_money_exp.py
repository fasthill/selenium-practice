# Task #3 Clean our data!
from bs4 import BeautifulSoup as bs
import requests
from module_collection import get_info_box, save_data, load_data, minute_to_integer
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

def money_conversion(money):
    pattern = re.compile(r'\$(\d{1,3}([,.]*\d{1,3})*)\s*(mil)*')
    try:
        result = re.search(pattern, money)
        quantity = result.group(1)
        quantity = quantity.replace(",","")  # delete comma in string
        money_val = float(quantity)
        if result.group(3) == 'mil':
            money_val = money_val * 1_000_000
        return f'{money_val:,}'  # insert comma for thousand separator
    except:
        return 'None'

#$30.9 million est. ₹ 79.43 crore (US$11 million)  ₹ 83 crore ['est.', '₹2,024–2,100 crore', '(', '$311–340\xa0million', ')']
# $7.7
#  million

money_box_office = [mv.get('Box office', 'None') for mv in movie_info_list]

for mv in movie_info_list:
    mbo = mv.get('Box office', 'N/A')
    result = money_conversion(mbo)
    mv['Box office (convert)'] = result

save_data('data/disney_datam.json', movie_info_list)
