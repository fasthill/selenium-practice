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
soup = bs(r.content)
# Print out the HTML
contents = soup.prettify()
# print(contents)

# info_box = soup.find(class_='infobox vevent')
info_box = soup.find('table', attrs={'class':'infobox vevent'})

info_rows = info_box.find_all('tr')

for row in info_rows:
    # print('{%s} : {%s}'.format(tr.th.text, tr.td.a.text ))


