from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
#기본군사훈련단
#url = 'https://www.airforce.mil.kr/user/indexSub.action?codyMenuSeq=156893223&siteId=last2&menuUIType=sub'
#군수 1학교
url = 'https://www.airforce.mil.kr/user/indexSub.action?codyMenuSeq=157620025&siteId=gisool2&menuUIType=sub'

driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

#정보 입력 창
driver.find_element_by_css_selector('#searchName').send_keys('이름')
driver.find_element_by_css_selector('#birthYear').send_keys('생년')
driver.find_element_by_css_selector('#birthMonth').send_keys('월')
driver.find_element_by_css_selector('#birthDay').send_keys('일')
driver.find_element_by_css_selector('#btnNext').click()

time.sleep(2)

#팝업에서 훈련병 선택
driver.switch_to_window(driver.window_handles[1])
driver.find_element_by_css_selector('.choice').click()

time.sleep(2)

#편지쓰기
driver.switch_to_window(driver.window_handles[0])
driver.find_element_by_css_selector('#btnNext').click()

time.sleep(2)

#인터넷편지 작성
driver.find_element_by_xpath("//div[@class='UIbtn']/span[@class='wizBtn large Ngray normal btnR']").click()

time.sleep(2)

#우편번호 및 주소(디폴트 유현욱 자취방)
driver.find_element_by_css_selector('#senderZipcode').click()

time.sleep(2)

driver.switch_to_window(driver.window_handles[1])

driver.find_element_by_css_selector('.popSearchInput').send_keys("상도로53길 45-6")

driver.find_element_by_xpath("/html/body/form[2]/div/div/div[1]/div[1]/fieldset/span/input[2]").click() #검색 버튼
driver.find_element_by_xpath("/html/body/form[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/a/div/div").click() #첫번째 목록 선택 목록 여러개면 div[]로 선택 가능할듯

time.sleep(1)

driver.find_element_by_css_selector('#rtAddrDetail').send_keys("101호")
driver.find_element_by_css_selector('.btn-bl').click()

#팝업 창에서 원래 창으로 이동
driver.switch_to_window(driver.window_handles[0])

driver.find_element_by_css_selector('#senderName').send_keys("소난다") #이름
driver.find_element_by_css_selector('#relationship').send_keys("울지마요") #관계
driver.find_element_by_css_selector('#title').send_keys("실패한 페이지를 확인하기 어렵네요") #제목
driver.find_element_by_css_selector('#contents').send_keys("안녕하세요. 용민이 인편지기였던 이규원입니다. 셀레니움 예외처리를 하는중입니다. 군대 들어가기 하루전에 이러는건 에바인가요?")  #내용 #1200자
driver.find_element_by_css_selector('#password').send_keys("1234") #비밀번호 #비밀번호 다르게 해야될까? 아니면 master key마냥 하나로 쭉 가도 안전할까?

driver.find_element_by_css_selector('.submit').click() #작성 완료

#근데 이게 가끔 작성 완료가 안될 때가 있거든? 그걸 어떻게 예외 처리해야할지 고민중...

cur_url = driver.current_url

print('응애!!!!!!')
print(driver.current_url)
print(cur_url)
if(cur_url.find('saveEmailSuccess') != -1):
    print('성공했으요!')
else:
    print('실패했으요')

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/span/input").click() #목록으로