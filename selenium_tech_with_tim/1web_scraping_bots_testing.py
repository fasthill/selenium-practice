# Selenium Tutorial #1
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# https://selenium-python.readthedocs.io/waits.html # selenium waits
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = '../selenium_Tacademy/chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
# print(driver.title)

# find id first, name second and class lastly.
search = driver.find_element_by_name('s')
search.send_keys('test')
search.send_keys(Keys.RETURN)

# main = driver.find_element_by_id('main') # 아래 내용으로 대체하면서 time.sleep()도 필요없음.
# time.sleep(5)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name('article')
    for article in articles:
        header = article.find_element_by_class_name('entry-summary')
        print(header.text)

except:
    driver.quit()

# print(main.text)
# print(driver.page_source)

driver.quit()
