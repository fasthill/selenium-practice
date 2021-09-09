from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://selenium-python.readthedocs.io/api.html , see section 7.2 Action Chains

PATH = '../selenium_Tacademy/chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.set_window_size(1024, 700)
driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(5)
cookie = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id('cookies')
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie) # actions.perform()에 의하여 수행됨.

for i in range(500):
    actions.perform() # cookie.click()과 동일한 결과를 보이나 속도면에서는 매우 느림. .click()이 빠름.
    time.sleep(0.05)
    count = int(cookie_count.text.split(" ")[0])
    print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()

driver.quit()