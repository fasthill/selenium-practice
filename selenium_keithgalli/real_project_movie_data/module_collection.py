from bs4 import BeautifulSoup as bs
import requests
import json

def get_content_value(row_data):
    if row_data.find('li'):
        return [li.get_text(" ", strip=True).replace('\xa0', ' ') for li in row_data.find_all('li')]
    elif row_data.find('br'):
        return [text for text in row_data.stripped_strings]  # make strings into list seperated by 'br'
    else:
        # text = row_data.get_text(" ", strip=True).replace('\xa0', ' ')  # replace special characters
        # try:
        #     if text.split(' ')[1] == 'minutes' :
        #         return int(text.split(' ')[0])
        # except:
        #     pass
        return row_data.get_text(" ", strip=True).replace('\xa0', ' ')

    # else:
        # if len(row_data.find_all('a')) > 1:
        #     return [a.get_text(" ", strip=True).replace('\xa0', ' ') for a in row_data.find_all('a')]
        # else:
        #     return row_data.get_text(" ", strip=True).replace('\xa0', ' ')  # replace special characters

def clean_tags(soup):
    for tag in soup.find_all('sup'):  # remove unnecessary tag with 'sup' which contains superscript like [1] [3] ...
        tag.decompose()
    for tag in soup.find_all('span', {'style': 'display:none'}):  # remove unnecessary tag with 'span display:none'
        tag.decompose()

def get_info_box(url):
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    info_box = soup.find('table', attrs={'class': 'infobox vevent'})
    info_rows = info_box.find_all('tr')

    clean_tags(soup)

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

def save_data(title, data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data(title):
    with open(title, 'r', encoding='utf-8') as f:
        return json.load(f)

# "85 minutes" => 85
def minute_to_integer(running_time):
    if running_time == 'N/A':
        return None

    if isinstance(running_time, list):
        return int(running_time[0].split(" ")[0])
    else:
        return int(running_time.split(" ")[0])

if __name__ == '__main__':
    print(minute_to_integer(['85 minutes', '100 minutes']))
    print(minute_to_integer('N/A'))