# 인터파크 투어 사이트에서 여행지를 입력후 검색(로그인) -> 잠시후 -> 결과
# 로그인시 PC 웹사이트에서 처리가 어려울 경우 -> 모바일 로그린으로 진입 ->
# 모듈 가져오기
# pip install selenium

from selenium import webdriver as wd

# 사전에 필요한 정보를 로드 => 디비 혹은 쉘, 배치 파일에서 인자로 받아서 세팅
main_url = 'https://tour.interpark.com/'
keyword = '로마'

# 드라이버 로드 : ChromeDriver - WebDriver for Chrome 을 찾아 윈도우용으로 받아서 현재 폴더에 저장
driver = wd.Chrome(executable_path='chromedriver.exe')
# 차후 -> 옵션 부여하여 (프록시, 에이전트 조작, 이미지를 배제(속도 증가효과))
# 크롤링을 오래 돌리면 -> temp에 임시파일들이 쌓인다! -> 템프 파일 삭제

# 사이트 접속 (get)
driver.get(main_url)
# 검색창을 찾아서 검색어를 입력
# 여기에 대기하는 웨이트를 걸어야 함.
# "id : SearchGNBText" 임을 확인 <- chrome 검사에서 확인
driver.find_element_by_id('SearchGNBText').send_keys(keyword) # 검색단어 입력
# 검색버튼을 클릭
# 잠시 대기 => 페이지가 로드되고 나서 즉각적으로 데이터를 획들하는 행위는 자제하시기 바랍니다.
# 이유는 ? 페이지가 변경되면 기다린다.(로드될 때까지 기다림. 평균 10초)