# keithGalli's youtube => https://www.youtube.com/watch?v=Ewgy-G9cmbg
# Scrape & clean a list of disney wikipedia pages to create a dataset to further analyze

# Task #1 Get into Box (store in Python dictionary)

# import necessary Libraries
from bs4 import BeautifulSoup as bs
import requests
from module_collection import get_content_value, get_info_box, save_data
import json

# Load the webpage
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
save_data('data/disney_data.json', movie_info_list)
