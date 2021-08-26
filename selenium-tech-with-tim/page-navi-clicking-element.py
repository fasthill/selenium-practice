from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# 크롬 자동 테스트를 회피하기 위한 import
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil

# # 여기서부터 회피 코드 삽입
# try:
#     shutil.rmtree(r"c://chrometemp")  #쿠키 / 캐쉬파일 삭제
# except FileNotFoundError:
#     pass
#
# subprocess.Popen(
#     r'C:\Program Files\Google\Chrome\Application\chrome.exe '
#     r'--remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동
#
# option = Options()
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#
# chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
# try:
#     driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
# except:
#     chromedriver_autoinstaller.install(True)
#     driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
# driver.implicitly_wait(10)
# # 여기까지 회피 코드

PATH = '../selenium-Tacademy/chromedriver.exe'
options = Options()
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options, executable_path=PATH)
# PATH = '../selenium-Tacademy/chromedriver.exe'
# driver = webdriver.Chrome(PATH, options=options)

# PATH = '../selenium-Tacademy/chromedriver.exe'
# chrome_options = webdriver.ChromeOptions();
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
# driver = webdriver.Chrome(options=chrome_options);

# PATH = '../selenium-Tacademy/chromedriver.exe'
# driver = webdriver.Chrome(PATH)


driver.set_window_size(1024, 600)

driver.get('https://techwithtim.net')

link = driver.find_element_by_partial_link_text('Python Programming')
link.click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()
except:
    driver.quit()