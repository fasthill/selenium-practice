from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = wd.Chrome(executable_path='selenium-Tacademy/chromedriver.exe')

driver.implicitly_wait(10)

""" naver example 
driver.get("https://naver.com")

# button = driver.find_element_by_css_selector('#search_btn')
button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#search_btn')))
button.click()
"""

# expedia example, https://www.youtube.com/watch?v=JfoTK3QBWYs
driver.get('https://www.expedia.com/')

#driver.find_element_by_id('tab-flight-tab-hp').click()
driver.find_element(By.ID, 'tab-flight-tav-hp').click()