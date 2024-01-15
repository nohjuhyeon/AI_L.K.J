# ## dbmongo의 collection 연결
# from pymongo import MongoClient
# mongoClient = MongoClient("mongodb://localhost:27017")
# # database 연결
# database = mongoClient["gatheringdatas"]
# # collection 작업
# collection = database['watcha_comments']
# collection.delete_many({})

# * 웹 크롤링 동작
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
import time
# ChromeDriver 실행

from selenium.webdriver.chrome.options import Options

# Chrome 브라우저 옵션 생성
chrome_options = Options()

# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# WebDriver 생성
webdriver_manager_dricetory = ChromeDriverManager().install()

browser = webdriver.Chrome(service = ChromeService(webdriver_manager_directory), options=chrome_options)                        # - chrome browser 열기

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

pass
browser.get("https://www.kobus.co.kr/oprninf/alcninqr/oprnAlcnPage.do")                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)

from selenium.webdriver.common.by import By          # - 정보 획득
# browser.save_screenshot('./formats.png')           


local_depart = "div.area_scroll.scrollbar-inner.scroll-content > ul > li:nth-child(2) > span"   # 서울
local_arrive = "div.area_scroll.scrollbar-inner.scroll-content > ul > li:nth-child(9) > span"   # 부산
local_list = "ul#tableTrmList > li> span"   # 리스트 목록
button_search = "#alcnSrchBtn > button" # 조회하기 버튼
time_depart = "#alcnList > p > span.start_time" # 출발시간

element_depart = browser.find_element(by = By.CSS_SELECTOR, value = local_depart)
element_arrive = browser.find_element(by = By.CSS_SELECTOR, value = local_arrive)
element_depart_list = browser.find_elements(by = By.CSS_SELECTOR, value = local_list)
element_arrive_list = browser.find_elements(by = By.CSS_SELECTOR, value = local_list)
element_search = browser.find_element(by = By.CSS_SELECTOR, value = button_search)
element_time = browser.find_elements(by = By.CSS_SELECTOR, value = time_depart)



while True :
    
    element_depart.click()  # 출발지 클릭
   
    for x in range(element_depart_list):
        element_depart_list[x].click()                 # 출발지 리스트 하나씩 클릭
        
        element_arrive.click    # 도착지 클릭
        for y in range(element_arrive_list):
            element_arrive_list[y].click()      # 도착지 리스트 하나씩 클릭
            element_search.click()   # 조회하기 클릭
            


# for x in range(element_list) :  

    browser.quit()                                      # - 브라우저 종료
