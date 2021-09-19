# get movie rating from db.
# use http://www.omdbapi.com/
# http://www.omdbapi.com/?i=tt3896198&apikey=1910a0fd
# http://www.omdbapi.com/?apikey=[yourkey]&
# apikey hide : 고급시스템설정 -> 시스템 속성 -> 환경변수 > 시스템변수 -> 새로만들기 -> 변수명, 값입력
# os.environ['변수명'] <- 값을 대체 (비밀번호일 경우 시스템변수 사용)

from module_collection import save_data_pickle, load_data_pickle
from module_get_rating_from_db_api import get_rating_db

movie_info_list = load_data_pickle('data/disney_datad.pkl')

movie_info_list_temp = []
for movie in movie_info_list:
    title = movie.get('title', 'N/A')
    if title == 'N/A':
        continue  #
    date = movie.get('Release date (datetime)', 'N/A')
    if date == 'N/A':
        continue  #
    print(f'title: {title}, date: {date}')
    if date == None:
        rating_value = get_rating_db(title)
    else:
        year = date.strftime('%Y')
        rating_value = get_rating_db(title, year)
    imdb_rating = rating_value[0]
    rotten_value = rating_value[1]
    movie['Rating (imdb)'] = imdb_rating
    movie['Value (rotten_tomatoes)'] = rotten_value
    movie_info_list_temp.append(movie)
    print('IMDB Rating ', rating_value[0],
          'Rotten Value ', rating_value[1])

save_data_pickle('data/disney_data_score_api.pkl', movie_info_list_temp)
# save_data('data/disney_datad.json', movie_info_list_temp)  # can't write datetime object into json.
# movie_info_list = load_data_pickle('data/disney_data_score_api.pkl')
