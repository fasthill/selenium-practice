from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# title = 'Dumbo' ; year = 1941  # worked
# title = 'Make Mine Music' ; year = 1946  # worked
# title = 'Westward Ho, the Wagons!' ; year = 1956 # different name, in imdb, there is a comma after 'Ho', whereas no comma in the movie list in hollywood list.

def get_movie_score(title, year):
    PATH = './chromedriver.exe'
    # options = webdriver.ChromeOptions()  # 옵션 생성
    # options.add_argument("--headless")  # 창 숨기는 옵션 추가
    # driver = webdriver.Chrome(PATH, options=options)
    driver = webdriver.Chrome(PATH)
    driver.set_window_position(-10000, 0)  # 창을 보이지 않게 함.
    # driver.set_window_size(1024, 700)
    driver.get('https://www.imdb.com/')
    time.sleep(1)
    print("____________enter def________________")
    year = str(year)
    driver.find_element_by_id('suggestion-search').clear()  # clear the input in case.
    driver.find_element_by_id('suggestion-search').send_keys(title)
    driver.find_element_by_id('suggestion-search-button').click()

    result_text = driver.find_elements_by_css_selector('div#main > div.article > div.findSection '
                                              '> table.findList > tbody > tr > td.result_text')

    for rt in result_text:
        try:
            if rt.text.split(' (')[0] == title:
                yr = rt.text.split(' (')[1].rstrip(')')
                try:
                    if yr == year:
                        print("GOOD", title, yr)
                        rt.find_element_by_tag_name('a').click()
                        time.sleep(1)
                        score = driver.find_elements_by_css_selector(
                            'div.AggregateRatingButton__ContentWrap-sc-1ll29m0-0.hmJkIS > div span')[0].text
                        base = driver.find_elements_by_css_selector(
                            'div.AggregateRatingButton__ContentWrap-sc-1ll29m0-0.hmJkIS > div span')[1].text.lstrip('/')
                        print(f'score : , {score}/{base}')
                        driver.close()
                        driver.quit()
                        return score, base
                except:
                    print("inner if")
                    pass
        except:
            print("outer if")
            pass
if __name__ == '__main__':
    title = 'So Dear to My Heart'
    year = 1948
    get_movie_score(title, year)