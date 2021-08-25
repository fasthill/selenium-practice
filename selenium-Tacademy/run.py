# 인터파크 투어 사이트에서 여행지를 입력후 검색(로그인) -> 잠시후 -> 결과
# 로그인시 PC 웹사이트에서 처리가 어려울 경우 -> 모바일 로그린으로 진입 ->
# 모듈 가져오기
# pip install selenium

from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
# import pymysql as my : DbMgr에서 사용
from DbMgr import DBHelper as Db
db = Db()
# 0. 사전에 필요한 정보를 로드 => 디비 혹은 쉘, 배치 파일에서 인자로 받아서 세팅
main_url = 'https://tour.interpark.com/'
keyword = '로마'
# 상품정보를 담는 리스트 (tour_list)
from Tour import TourInfo

tour_list = []

# 1. 드라이버 로드 : ChromeDriver - WebDriver for Chrome 을 찾아 윈도우용으로 받아서 현재 폴더에 저장
driver = wd.Chrome(executable_path='chromedriver.exe')
# 차후 -> 옵션 부여하여 (프록시, 에이전트 조작, 이미지를 배제(속도 증가효과))
# 크롤링을 오래 돌리면 -> temp에 임시파일들이 쌓인다! -> 템프 파일 삭제

# 2. 사이트 접속 (get)
driver.get(main_url)
# 3. 검색창을 찾아서 검색어를 입력
# 여기에 대기하는 웨이트를 걸어야 함.
# "id : SearchGNBText" 임을 확인 <- chrome 검사에서 확인
driver.find_element_by_id('SearchGNBText').send_keys(keyword)  # 검색단어 입력
# 수정할 경우 => 뒤에 내용이 붙어 버림. 새로운 내용을 집어 넣고자 할때 문제 발생
# => 그래서 .clear() 후에 -> send.keys('내용') 으로 진행해야 함.
# driver.find_element_by_id('SearchGNBText').send_keys('파리') # 진행하면 => 검색어가 '로마파리' 진행됨.
# driver.find_element_by_id('SearchGNBText').clear()
# driver.find_element_by_id('SearchGNBText').send_keys('파리')
# 4. 검색버튼을 클릭
driver.find_element_by_css_selector('.search-btn').click()  # class 명칭이 'search-btn' 인경우가 하나밖에 없어서 가능
#                                                            그렇지 않을 경우 'button.search-btn' 기입해야 함.

# 5. 잠시 대기 => 페이지가 로드되고 나서 즉각적으로 데이터를 획들하는 행위는 자제하시기 바랍니다.
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
        # 지정한 한 개 요소가 올라오면 웨이트를 종료
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
driver.implicitly_wait(10)  # 10초 대기
# 절대적 대기 => time.sleep() 무조건 대기, -> 클라우드 페어(DDOS 방어 솔루션)
# 이유는 ? 페이지가 변경되면 기다린다.(로드될 때까지 기다림. 평균 10초)
# 6. 더 보기 누르기 => 게시판 진입

driver.find_element_by_css_selector('div.oTravelBox > ul.boxList > li.moreBtnWrap > button.moreBtn').click()
# driver.find_element_by_css_selector('div.oTravelBox > ul.boxList > li.moreBtnWrap > button.moreBtn')

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

numpage = 1  # 데스트를 위하여 7에서 임시로 1개만 갖고 테스트
for page in range(1, 1 + numpage):
    try:
        # 자바 스크립트 구동하기
        # driver.execute_script("searchModule.SetCategoryList(%s, '') " % page)  # 실행될 때마다 페이지가 새로 발생함
        # time.sleep(2) # 강제로 2초씩 쉼. 페이지가 생길 때 사용되는 시간을 기다림.(명시적, 묵시적 방법도 사용할 수 있음)

        # 위 두개의 command보다 아래 Explicit wait  이용
        try:
            ele = WebDriverWait(driver, 10).until(
                    driver.execute_script("searchModule.SetCategoryList(%s, '') " % page))
                # lambda driver: driver.execute_script("searchModule.SetCategoryList(%s, '') " % page))
            # 대기 시간 10초, 끝나면 10초 전이라도 실행함.
        except Exception as e:
            print('오류 발생', e)
        print("%s 페이지 이동" % page)
        #################
        # 여러사이트에서 정보를 수집할 경우, 공통정보 정의 단계 필요
        # 상품명, 코멘트, 기간1, 기간2, 가격, 평점, 섬네일, 링크(상품상세정보)
        boxItems = driver.find_elements_by_css_selector('div.oTravelBox>ul.boxList>li.boxItem') # elements 복수에 유의
        print("2 페이지 이동")
        # 상품 하나 하나 접근
        for li in boxItems:
            print("33 페이지 이동")
            prod_name = li.find_element_by_css_selector('.boxTables > div.title-row h5.proTit').text
            print("34 페이지 이동")
            comment = li.find_element_by_css_selector('.boxTables > div.title-row p.proSub').text
            print("35 페이지 이동")
            price = li.find_element_by_css_selector('.boxTables > div.title-row strong.proPrice').text
            schedule1 = li.find_elements_by_css_selector('.boxTables > div.info-row > div > p.proInfo')[0].text
            schedule2 = li.find_elements_by_css_selector('.boxTables > div.info-row > div > p.proInfo')[1].text
            grade = li.find_element_by_css_selector('.boxTables > div.info-row > div > .proSpeacial ~p.proInfo').text
            print('상품명: ', prod_name)
            print('코멘트: ', comment)
            print('가격: ', price)
            print('기간1: ', schedule1)
            print('기간2: ', schedule2)
            print('평점: ', grade)
            print("3 페이지 이동")
            # 이미지를 링크값을 사용할 것인가?
            # 직접 다운로드 해서 우리 서버에 업로드(ftp) 할 것인가?
            thumbn = li.find_element_by_css_selector('a > img').get_attribute('src')
            print("4 페이지 이동")
            print('섬네일: ', thumbn)
            # print('링크: ', li.find_element_by_css_selector('a').get_attribute('onclick').split("'")[1])
            link = li.find_element_by_css_selector('a').get_attribute('onclick')
            print("5 페이지 이동")
            print('링크: ', link)
            # li.find_element_by_css_selector('a').click() # 새 창 pop up, 그런데 새창의 정보는 어떻게 가져오는가?
            # driver.implicitly_wait(10) # 10초 대기 # implicit wait는 한 번만 declare 하면 됨.

            # dtest = driver.find_element_by_css_selector('.swiper-containerz guide-info section .guide span')
            # print('가이드: ', dtest.text)
            # driver.execute_script("searchModule.OnClickDetail('http://tour.interpark.com/goods/detail/?BaseGoodsCd=A3015008', '')")
            # print("새링크",driver1.find_element_by_css_selector('.score > .point01').text)

            print('=' * 70)
            obj = TourInfo(prod_name, price, schedule2, link, thumbn)
            tour_list.append(obj)

    except Exception as e1:
        print("오류", e1)

    print(len(tour_list))
    # 수집한 정보 갯수를 루프 => 페이지 방문 => 콘텐츠 획득(상품상세정보) => DB까지..
    for tour in tour_list:
        # tour = TourInfo
        print(type(tour))
        # 링크 데이터에서 실데이터 획득
        # 분해
        arr = tour.link.split(',')
        # 대체
        if arr:
            # 대체
            link = arr[0].replace('searchModule.OnClickDetail(', '')
            # 슬라이싱 => 앞의 ',', 뒤의 ',' 제거
            detail_url = link[1:-1]
            # 상세 페이지 이름 : URL 값이 완성된 형태인지 확인 필요(hrrp~)
            print("6 페이지 이동")
            driver.get(detail_url)
            time.sleep(2)
            print("7 페이지 이동")
            # beautifulsoup 설치 이용
            # 현재 페이지를 beautifulesoup의 DOM으로 구성
            soup = bs(driver.page_source, 'html.parser')
            # 현재 상세정보 페이지에서 스케쥴 정보 획득
            #data = soup.select('.schedule-all')
            data = soup.select('.schedule-all')
            print(type(data), len(data))
            # dBody > div.default-section.goods-info > div.info-list > div.goods-point.section > ul
            # 디비 입력 => pymysql 활용 => pip install pymysql
            content = data[0].select_one('h3').text
            print("contents:", content)
            #contents 내용에 따라서 전처리가 필요할 수 있음.
            db.db_insertCrawlingData(
                tour.title,
                tour.price,
                tour.area,
                content,
                keyword
            )




    # 종료 , 아래 내용은 반드시 실행해야 함. 프로그램할 때 아래 내용 미리 기입해 놓고 작성하는 것이 좋음.
    driver.close()
    driver.quit()
    import sys

    sys.exit()
