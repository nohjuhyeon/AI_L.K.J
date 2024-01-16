def connection() :                                                                                      # mongo DB 연결
    from pymongo import MongoClient
    mongoClient = MongoClient("mongodb://192.168.10.240:27017/")
    # database 연결
    database = mongoClient["AI_LKJ"]
    # collection 작업
    collection = database['reserve_transfer_bus']
    # collection.delete_many({})
    return collection

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

# 검색 전

button_depart = "#readDeprInfoList > p"    # 출발지
local_depart = "div.area_scroll.scrollbar-inner.scroll-content > ul > li:nth-child(2) > span"       # 서울
local_arrive = "div.area_scroll.scrollbar-inner.scroll-content > ul > li:nth-child(9) > span"       # 부산
local_list = "ul#tableTrmList > li> span"                                                           # 리스트 목록
button_search = "#alcnSrchBtn > button"                                                             # 조회하기 버튼
time_depart = "#alcnList > p > span.start_time"                                                     # 출발시간
day_depart = "#ui-datepicker-div > table > tbody > tr:nth-child(3) > td:nth-child(7) > a"           # 20일
day_calender = "p > img"                                                                            # 달력

element_button_depart = browser.find_element(by = By.CSS_SELECTOR, value = button_depart)
element_local_depart = browser.find_element(by = By.CSS_SELECTOR, value = local_depart)
element_local_arrive = browser.find_element(by = By.CSS_SELECTOR, value = local_arrive)
element_depart_list = browser.find_elements(by = By.CSS_SELECTOR, value = local_list)
element_arrive_list = browser.find_elements(by = By.CSS_SELECTOR, value = local_list)
element_search = browser.find_element(by = By.CSS_SELECTOR, value = button_search)
element_time = browser.find_elements(by = By.CSS_SELECTOR, value = time_depart)
element_day_depart = browser.find_element(by = By.CSS_SELECTOR, value = day_depart)
element_day_calender = browser.find_element(by = By.CSS_SELECTOR, value = day_calender)

# 검색 후(스크래핑)
name_depart = "#readDeprInfoList > p"                                                               # 출발지 이름
element_name_depart = browser.find_element(by = By.CSS_SELECTOR, value = name_depart)
name_arrive = "#readArvlInfoList > p"                                                               # 도착지 이름
element_name_arrive = browser.find_element(by = By.CSS_SELECTOR, value = name_arrive)
time_depart = "#alcnList > p > span.start_time"                                                     # 출발시간
element_time_depart = browser.find_elements(by = By.CSS_SELECTOR, value = time_depart)

bus_group ="span.bus_com > span.dyexpress"                                                          # 고속사 이름
element_bus_group = browser.find_elements(by = By.CSS_SELECTOR, value = bus_group)
charge_adult = "#alcnList > p > span.adult"                                                         # 어른 요금
element_charge_adult = browser.find_elements(by = By.CSS_SELECTOR, value = charge_adult)
charge_child = "#alcnList > p > span.child"                                                         # 초등생 요금
element_charge_child = browser.find_elements(by = By.CSS_SELECTOR, value = charge_child)
charge_youth = "#alcnList > p > span.youth"                                                         # 중고생 요금
element_charge_youth = browser.find_elements(by = By.CSS_SELECTOR, value = charge_youth)

from selenium.common.exceptions import NoSuchElementException
import pyautogui

element_day_calender.click()    # 달력 누르기
time.sleep(2)
element_day_depart = browser.find_element(by = By.CSS_SELECTOR, value = day_depart)
element_day_depart.click()  # 20일 누르기

while True :
    element_button_depart.click()   # 출발지 클릭
    pass
    element_local_depart.click()    # 서울 클릭
    
    element_depart_list = browser.find_elements(by = By.CSS_SELECTOR, value = local_list)
    for x in range(len(element_depart_list)):
        element_depart_list = browser.find_elements(by = By.CSS_SELECTOR, value = local_list)
        pass
        element_depart_list[x].click()                 # 서울의 출발지 리스트 하나씩 클릭

        element_local_arrive.click()    # 부산 클릭
        element_arrive_list = browser.find_elements(by = By.CSS_SELECTOR, value = local_list)
        for y in range(len(element_arrive_list)):
            element_arrive_list = browser.find_elements(by = By.CSS_SELECTOR, value = local_list)
            time.sleep(1)
            element_arrive_list[y].click()      # 도착지 리스트 하나씩 클릭
            time.sleep(1)
            element_search.click()   # 조회하기 클릭
            time.sleep(2)

            element_name_depart = browser.find_element(by = By.CSS_SELECTOR, value = name_depart)           #데이터 출력
            element_name_arrive = browser.find_element(by = By.CSS_SELECTOR, value = name_arrive)
            element_time_depart = browser.find_elements(by = By.CSS_SELECTOR, value = time_depart)
            # element_bus_group = browser.find_elements(by = By.CSS_SELECTOR, value = bus_group)
            # element_charge_adult = browser.find_elements(by = By.CSS_SELECTOR, value = charge_adult)
            # element_charge_child = browser.find_elements(by = By.CSS_SELECTOR, value = charge_child)
            # element_charge_youth = browser.find_elements(by = By.CSS_SELECTOR, value = charge_youth)
            for element_time in element_time_depart :
                element_time_depart = browser.find_elements(by = By.CSS_SELECTOR, value = time_depart)  
                element_name_arrive = browser.find_element(by = By.CSS_SELECTOR, value = name_arrive)
                element_time_depart = browser.find_elements(by = By.CSS_SELECTOR, value = time_depart)
                # element_bus_group = browser.find_elements(by = By.CSS_SELECTOR, value = bus_group)
                # element_charge_adult = browser.find_elements(by = By.CSS_SELECTOR, value = charge_adult)
                # element_charge_child = browser.find_elements(by = By.CSS_SELECTOR, value = charge_child)
                # element_charge_youth = browser.find_elements(by = By.CSS_SELECTOR, value = charge_youth)
                
                result_element_name_depart = element_name_depart.text
                result_element_name_arrive = element_name_arrive.text
                result_element_time_depart = element_time.text 
                # result_element_bus_group = element_bus_group.text
                # result_element_charge_adult = element_charge_adult.text
                # element_charge_child.text
                # element_charge_youth.text



                
                print("출발지 : {}, 도착지 : {}, 출발시간 : {}".format(result_element_name_depart,result_element_name_arrive,result_element_time_depart))
                print("고속사 : {}, 어른요금 : {}, 초등생요금 : {}, 중고생요금 : {}".format(element_bus_group,element_charge_adult,element_charge_child,element_charge_youth))
                pass
                # collection_database = connection()
                # collection_database.insert_one({"출발지" : result_element_name_depart , "도착지" : result_element_name_arrive, "출발시간" : result_element_time_depart, 
                #                                 "고속사" : element_bus_group, "어른요금" : element_charge_adult, "초등생요금":  element_charge_child, "중고생요금" : element_charge_youth})

            try : 
                 # 출발지 클릭 (다시 실행)
                element_button_depart.click() 
                time.sleep(1)
            except :
                pyautogui.press('확인')
                
                time.sleep(1)

                element_button_depart.click() 
            finally : 
                pass
            element_local_depart.click()    # 서울 클릭
            time.sleep(1)
            
            if y < len(element_arrive_list)-1 :
                element_depart_list = browser.find_elements(by = By.CSS_SELECTOR, value = local_list)
                element_depart_list[x].click()             
                time.sleep(1)    # 서울의 출발지 리스트 하나씩 클릭
                element_local_arrive.click()    # 부산 클릭
            elif y == len(element_arrive_list)-1 :
                break
            




        




selector_value = "#alcnList > p"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value = selector_value)

# for x in range(element_list) :  

browser.quit()                                      # - 브라우저 종료
