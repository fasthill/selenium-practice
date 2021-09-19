# get movie rating from db.
# use http://www.omdbapi.com/
# http://www.omdbapi.com/?i=tt3896198&apikey=1910a0fd
# http://www.omdbapi.com/?apikey=[yourkey]&
# apikey hide : 고급시스템설정 -> 시스템 속성 -> 환경변수
# -> 시스템변수 -> 새로만들기 -> 변수명, 값입력  ## pc를 꼇다 켜야 인식함
# os.environ['변수명'] <- 값을 대체 (비밀번호일 경우 시스템변수 사용)

import json

import requests
import urllib
import os

def get_rating_db(title, year):
    print(f'Title: {title}, Year: {year}')
    base_url = 'https://www.omdbapi.com/?'
    parameters = {'apikey': os.environ['OMDB_API_KEY'], 't': title, 'y': year}  # get the parameter info in the api homepage
    params_encoded = urllib.parse.urlencode(parameters)
    full_url = base_url + params_encoded
    data_json = requests.get(full_url).json()
    imdb_rating = data_json.get('imdbRating', 'N/A')
    rotten_dict = data_json.get('Ratings', [])

    for dic_r in rotten_dict:
        if dic_r['Source'] == 'Rotten Tomatoes':
            rotten_value = dic_r.get('Value', 'N/A')
            return imdb_rating, rotten_value
    return imdb_rating, 'N/A'


if __name__ == '__main__':
    # title = 'Dumbo' ; year = 1941  # worked
    # title = 'Make Mine Music' ; year = 1946  # worked
    # title = 'Westward Ho, the Wagons!' ; year = 1956 # different name, in imdb, there is a comma after 'Ho', whereas no comma in the movie list in hollywood list.
    # title = 'Fun and Fancy Free' ;  year = str(1947)  # 1947 release 편은 데이터 없음.
    title = 'Scandalous John' ; year = '1971'
    rating_value = get_rating_db(title, year)
    print('def IMDB Rating ', rating_value[0],
          'Rotten Value ', rating_value[1])
