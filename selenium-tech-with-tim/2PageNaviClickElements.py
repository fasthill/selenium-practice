from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = '../selenium-Tacademy/chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.set_window_size(1024, 700)

driver.get('https://techwithtim.net')
time.sleep(1)

link = driver.find_element_by_link_text('Python Programming')
link.click()
# skip ad pop up logic. sometimes ads are popped up and can't bypass to the next step
driver.back()
driver.forward()
# ad pop up

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()
except WebDriverWait:
    driver.quit()

driver.quit()
