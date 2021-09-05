# keithGalli's youtube => https://www.youtube.com/watch?v=Ewgy-G9cmbg
# Scrape & clean a list of disney wikipedia pages to create a dataset to further analyze

# Task #1 Get into Box (store in Python dictionary)

# import necessary Libraries
from bs4 import BeautifulSoup as bs
import requests

# Load the webpage
URL = 'https://wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films'
URL = 'https://en.wikipedia.org/wiki/Toy_Story_3'
r = requests.get(URL)
# convert to beautifulsoup object
soup = bs(r.content, 'html.parser')
# Print out the HTML
contents = soup.prettify()
# print(contents)

# info_box = soup.find(class_='infobox vevent')
info_box = soup.find('table', attrs={'class': 'infobox vevent'})

info_rows = info_box.find_all('tr')

# for row in info_rows:
#     print(row.prettify())

def get_content_value(row_data):
    if row_data.find('li'):
        return [li.get_text(" ", strip=True).replace('\xa0', ' ') for li in row_data.find_all('li')]
    else:
        return row_data.get_text(" ", strip=True).replace('\xa0', ' ')  # replace special characters


movie_info = {}
for index, row in enumerate(info_rows):
    if index == 0:
        movie_info['title'] = row.find('th').get_text(" ", strip=True)
        # get_text change like line feed character to a space.
        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html?highlight=get_text#get-text
    elif index == 1:
        continue
    else:
        content_key = row.find('th').get_text(" ", strip=True)
        content_value = get_content_value(row.find('td'))
        movie_info[content_key] = content_value

# for key, value in movie_info.items():
#     print('{} : {} '.format(key, value))

# Task 2: Get info box for all movies
URL = 'https://wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films'
r = requests.get(URL)
# convert to beautifulsoup object
soup = bs(r.content, 'html.parser')
# Print out the HTML
contents = soup.prettify()
# print(contents)

movies = soup.select("table.wikitable.sortable i a")
# print(movies)

def get_content_value(row_data):
    if row_data.find('li'):
        return [li.get_text(" ", strip=True).replace('\xa0', ' ') for li in row_data.find_all('li')]
    else:
        return row_data.get_text(" ", strip=True).replace('\xa0', ' ')  # replace special characters

def get_info_box(url):
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    info_box = soup.find('table', attrs={'class': 'infobox vevent'})
    info_rows = info_box.find_all('tr')
    movie_info = {}
    for index, row in enumerate(info_rows):
        if index == 0:
            movie_info['title'] = row.find('th').get_text(" ", strip=True)
            # get_text change like line feed character to a space.
            # https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html?highlight=get_text#get-text
        elif index == 1:
            continue
        else:
            content_key = row.find('th').get_text(" ", strip=True)
            content_value = get_content_value(row.find('td'))
            movie_info[content_key] = content_value

    return movie_info


base_path = 'https://en.wikipedia.org'
movie_info_list = []

for index, movie in enumerate(movies):
    # if index == 10: # we do not want all the iteration
    #     break
    try:
        relative_path = movie['href']
        full_path = base_path + relative_path
        if movie.get_text():
            title = movie.get_text()
        elif movie['title']:
            title = movie['title']

        movie_info_list.append(get_info_box(full_path))

    except Exception as e:
        print(movie.get_text())
        print(e, "error index num", index, movie)

# for i in movie_info_list:
#     print(i)

# Save/Reload Movie Data

import json

def save_data(title, data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data(title):
    with open(title, 'r', encoding='utf-8') as f:
        return json.load(f)

save_data('disney_data.json', movie_info_list)