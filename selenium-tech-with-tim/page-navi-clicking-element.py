from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup as bs
import requests

PATH = '../selenium-Tacademy/chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.set_window_size(1024, 600)

driver.get('https://techwithtim.net')

link = driver.find_element_by_partial_link_text('Python Programming')
print("wait")
time.sleep(3)
print("in")
link.click()
print("after click")
time.sleep(5)
print("out")
soup = bs(driver.page_source, 'html.parser')
print(soup.prettify())
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
#     )
#     element.click()
# except:
#     driver.quit()