## dbmongo의 collection 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.240:27017/AI_LKJ")

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
browser.get("https://www.skyscanner.co.kr/transport/flights/gmp/pus/240120/?adultsv2=4&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=true&ref=home&rtn=0")
pass
# html 파일 받음(and 확인)
html = browser.page_source
pass
# 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# #J_resultList> div
airport_list = browser.find_elements(by=By.CSS_SELECTOR,value = "div > div.UpperTicketBody_container__NDcwM")
time.sleep(2)
airport_name_list = []
airport_time_list = []
airport_content_list = []
for airport_item in airport_list :
    try :
        airport_name = airport_item.find_element(by=By.CSS_SELECTOR, value = "div.LogoImage_container__MDU0Z.LegLogo_logoContainer__ODdkM.UpperTicketBody_legLogo__ZjYwM > div > div > img")
        str_airport_name = airport_name.text
        pass
    except :
        str_airport_name = ""
    airport_name_list.append(str_airport_name)
    pass
    
    try :
        airport_time = airport_item.find_element(by=By.CSS_SELECTOR, value = "div > div.LegInfo_legInfo__ZGMzY")
        str_airport_time = airport_time.text
        pass
    except :
        str_airport_time = ""
    airport_time_list.append(str_airport_time)
    pass
    
    try :
        airport_content = airport_item.find_element(by=By.CSS_SELECTOR, value = "div.BpkTicket_bpk-ticket__paper__OTA1O.BpkTicket_bpk-ticket__stub__OTgwN.Ticket_stub__NGYxN.BpkTicket_bpk-ticket__stub--padded__YzM0N.BpkTicket_bpk-ticket__stub--horizontal__ZmQzY > div > div > div")
        str_airport_content = airport_content.text
        pass
    except :
        str_airport_content = ""
    airport_content_list.append(str_airport_content)
    pass

for i in range(len(airport_list)) :
    collection.insert_one({"항공사" : airport_name_list[i],
                          "소요시간" : airport_time_list[i],
                          "가격" : airport_content_list[i]})
pass
    
# 브라우저 종료
browser.quit()