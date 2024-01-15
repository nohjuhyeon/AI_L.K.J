## dbmongo의 collection 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.238:27017/")

# database 연결
database = mongoClient["AI_LKJ"]

# collection 작업
collection = database['reserve_transfer_airport']
collection.delete_many({})

# 웹 크롤링 동작
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

# 주소 입력
browser.get("https://kr.trip.com/flights/seoul-to-busan/tickets-sel-pus?dcity=sel&acity=pus&ddate=2024-01-20&rdate=2024-01-25&flighttype=rt&class=y&lowpricesource=searchform&quantity=4&searchboxarg=t&nonstoponly=off&locale=ko-KR&curr=KRW")
pass
# html 파일 받음(and 확인)
html = browser.page_source
pass
# 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# element_body = browser.find_element(by=By.CSS_SELECTOR,value="div.l-inner.m-main-inner.is-v2.clearfix")

airport_list = browser.find_elements(by=By.CSS_SELECTOR,value = "#J_resultList> div")
time.sleep(2)
airport_name_list = []
airport_time_list = []
airport_content_list = []
for airport_item in airport_list :
    try :
        airport_name = airport_item.find_element(by=By.CSS_SELECTOR, value = "div.flights-name")
        str_airport_name = airport_name.text
        pass
    except :
        str_airport_name = ""
    airport_name_list.append(str_airport_name)
    pass
    
    try :
        airport_time = airport_item.find_element(by=By.CSS_SELECTOR, value = "div.flight-info-col.col-2 > div")
        str_airport_time = airport_time.text
        pass
    except :
        str_airport_time = ""
    airport_time_list.append(str_airport_time)
    pass
    
    try :
        airport_content = airport_item.find_element(by=By.CSS_SELECTOR, value = "div.item-con-price_a7E")
        str_airport_content = airport_content.text
        pass
    except :
        str_airport_content = ""
    airport_content_list.append(str_airport_content)
    pass

# print
    
# 브라우저 종료
browser.quit()