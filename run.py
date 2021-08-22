# 인터파크 투어 사이트에서 여행지를 입력후 검색(로그인) -> 잠시후 -> 결과
# 로그인시 PC 웹사이트에서 처리가 어려울 경우 -> 모바일 로그린으로 진입 ->
# 모듈 가져오기
# pip install selenium

from selenium import webdriver as wd

#0. 사전에 필요한 정보를 로드 => 디비 혹은 쉘, 배치 파일에서 인자로 받아서 세팅
main_url = 'https://tour.interpark.com/'
keyword = '로마'

#1. 드라이버 로드 : ChromeDriver - WebDriver for Chrome 을 찾아 윈도우용으로 받아서 현재 폴더에 저장
driver = wd.Chrome(executable_path='chromedriver.exe')
# 차후 -> 옵션 부여하여 (프록시, 에이전트 조작, 이미지를 배제(속도 증가효과))
# 크롤링을 오래 돌리면 -> temp에 임시파일들이 쌓인다! -> 템프 파일 삭제

#2. 사이트 접속 (get)
driver.get(main_url)
#3. 검색창을 찾아서 검색어를 입력
# 여기에 대기하는 웨이트를 걸어야 함.
# "id : SearchGNBText" 임을 확인 <- chrome 검사에서 확인
driver.find_element_by_id('SearchGNBText').send_keys(keyword) # 검색단어 입력
# 수정할 경우 => 뒤에 내용이 붙어 버림. 새로운 내용을 집어 넣고자 할때 문제 발생
# => 그래서 .clear() 후에 -> send.keys('내용') 으로 진행해야 함.
# driver.find_element_by_id('SearchGNBText').send_keys('파리') # 진행하면 => 검색어가 '로마파리' 진행됨.
# driver.find_element_by_id('SearchGNBText').clear()
# driver.find_element_by_id('SearchGNBText').send_keys('파리')
#4. 검색버튼을 클릭
driver.find_element_by_css_selector('.search-btn').click() # class 명칭이 'search-btn' 인경우가 하나밖에 없어서 가능
                                                   # 그렇지 않을 경우 'button.search-btn' 기입해야 함.

#5. 잠시 대기 => 페이지가 로드되고 나서 즉각적으로 데이터를 획들하는 행위는 자제하시기 바랍니다.
# 참조 https://selenium-python.readthedocs.io/waits.html
# Explicit waits: 인스턴스가 발생할 때까지 wait,
# 화면가 화면이 넘어갈때는 반드시 사용해야 함. 페이지가 넘어갈 때는 반드시 해야 함
# 명시적 대기 => 특정 요소가 로케이트(발견될 때까지) 대기
# driver = webdriver.Firefox()
# driver.get("http://somedomain/url_that_delays_loading")
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#     )
# finally:
#     driver.quit()
from selenium.webdriver.common.by import By
# 명시적 대기를 위하여 아래 import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 위 모듈 import 필요 (https://selenium-python.readthedocs.io/waits.html 에서 paste)
try:
    element = WebDriverWait(driver, 10).until(
        #지정한 한 개 요소가 올라오면 웨이트를 종료
        EC.presence_of_element_located((By.CLASS_NAME, "oTravelBox"))
    )
    # 대기 시간 10초, 끝나면 10초 전이라도 실행함.
except Exception as e:
    print('오류 발생', e)

# Implicit Wait: 일정한 시간을 기다린 후 실행
# 암묵적 대기 => DOM이 다 로드될 때까지 대기하고 먼저 로드되면 바로 진행
# driver = webdriver.Firefox()
# driver.implicitly_wait(10) # seconds 10초를 기다리고 실행
# driver.get("http://somedomain/url_that_delays_loading")
# myDynamicElement = driver.find_element_by_id("myDynamicElement")
# 요소를 찾을 특정 시간 동안 DOM풀림을 지시. 예를 들어 10초 이내라고 발견 되면 바로 진행(명시적과 공통 사항)
driver.implicitly_wait(10) # 10초 대기
# 절대적 대기 => time.sleep() 무조건 대기, -> 클라우드 페어(DDOS 방어 솔루션)
# 이유는 ? 페이지가 변경되면 기다린다.(로드될 때까지 기다림. 평균 10초)
# 6. 더 보기 누르기 => 게시판 진입

driver.find_element_by_css_selector('div.oTravelBox > ul.boxList > li.moreBtnWrap > button.moreBtn').click()
#driver.find_element_by_css_selector('div.oTravelBox > ul.boxList > li.moreBtnWrap > button.moreBtn')

# 게시판에서 데이터를 가져올 때
# 데이터가 많으면 ㅔ션(혹시 로그린을 해서 접근되는 사이트일 경우) 관리
# 특정 단위별로 로그아웃 로그인을 게속 시도
# 특정 게시물이 사라질 경우 => 팝업 발생(없는글... 등) => 팝업 처리 검토 필요
# 단, 로그인도 하지 않고, 수집 데이터가 많지 않을 때는 위의 경우는 나타나지 않음. (몇백개 정도는 문제 없음.)
# 게시판을 스캔시 => 임계점을 모름!!
# 게시판을 스캔을 하여 메타 정보(전체갯수)를 획득을 하여 loop를 돌려서 일괄적으로 방문 접근 처리
# searchModule.SetCategoryList(1, '') 스크립트 실행 <= 웹페이지 검사에서 확인

# 6+1은 임시 값, 게시물을 넘어갔을 때 현상을 확인차 추가함(현재는 6개까지 표시됨)
import time
numpage = 1 # 데스트를 위하여 7에서 임시로 1개만 갖고 테스트
for page in range(1,1+numpage):
    try:
        # 자바 스크립트 구동하기
        driver.execute_script("searchModule.SetCategoryList(%s, '') " % page) # 실행될 때마다 페이지가 새로 발생함
        #time.sleep(2) # 강제로 2초씩 쉼. 페이지가 생길 때 사용되는 시간을 기다림.(명시적, 묵시적 방법도 사용할 수 있음)
        print("%s 페이지 이동" %page)
        #################
        # 여러사이트에서 정보를 수집할 경우, 공통정보 정의 단계 필요
        # 상품명, 코멘트, 기간1, 기간2, 가격, 평점, 섬네일, 링크(상품상세정보)
        boxItems = driver.find_elements_by_css_selector('div.oTravelBox>ul.boxList>li.boxItem') # elements 복수에 유의
        # 상품 하나 하나 접근
        for li in boxItems:
            print('상품명: ',li.find_element_by_css_selector('.boxTables > div.title-row h5.proTit').text)
            print('코멘트: ',li.find_element_by_css_selector('.boxTables > div.title-row p.proSub').text)
            print('가격: ',li.find_element_by_css_selector('.boxTables > div.title-row strong.proPrice').text)
            print('기간1: ', li.find_elements_by_css_selector('.boxTables > div.info-row > div > p.proInfo')[0].text)
            print('기간2: ', li.find_elements_by_css_selector('.boxTables > div.info-row > div > p.proInfo')[1].text)
            print('평점: ', li.find_element_by_css_selector('.boxTables > div.info-row > div > .proSpeacial ~p.proInfo').text)
            print('섬네일: ', li.find_element_by_css_selector('a > img').get_attribute('src'))
            #print('링크: ', li.find_element_by_css_selector('a').get_attribute('onclick').split("'")[1])
            print('링크: ', li.find_element_by_css_selector('a').get_attribute('onclick'))
            li.find_element_by_css_selector('a').click() # wait 관련 확인하고 진행해야 하는가?
            # driver.implicitly_wait(10) # 10초 대기
            try:
                element = WebDriverWait(driver, 10).until(
                    # 지정한 한 개 요소가 올라오면 웨이트를 종료
                    EC.presence_of_element_located((By.CLASS_NAME, "selc-date j-traffic"))
                    # 새 페이지에서 출발일 및 교통편 선택(class name: 'sec-date j-traffic')이 로딩될 때까지 wait 함
                )
                # 대기 시간 10초, 끝나면 10초 전이라도 실행함.
            except Exception as e:
                print('오류 발생', e)


            print('---------------------------------------------')


    except Exception as e1:
        print("오류", e1)
