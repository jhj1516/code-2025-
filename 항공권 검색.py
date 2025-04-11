import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 네이버 항공권 예약 페이지 열기
browser = webdriver.Chrome()
url = 'https://flight.naver.com/'
browser.get(url)

# 2. 광고 팝업 닫기
time.sleep(1) #1초 대기
seen = browser.find_element(By.XPATH, '//button[@class="FullscreenPopup_close"]')
seen.click()

# 3. 가는 날 버튼 클릭
begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_date.click()

# 4. 가는 날짜 선택
time.sleep(1)
day27 = browser.find_elements(By.XPATH, '//b[text() = "27"]')
day27[0].click()

# 5. 도착 날짜 선택
day30 = browser.find_elements(By.XPATH, '//b[text() = "30"]')
day30[0].click()

# 6. 도착 버튼 클릭
arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
arrival.click()

# 7. 도착 목적지 선택
dokyo = browser.find_element(By.XPATH, '//button[text() = "도쿄"]')
dokyo.click()

#8. 항공권 검색 시작
search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
search.click()

# 9. 내가 원하는 항공권(가격이 제일 싼)이 등장 할 때까지 기다리고 등장하면 출력
elem = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, '//div[@class="concurrent_RoundSameAL__8lC9z concurrent_item__wwwxh"]')))
print(elem.text)

browser.quit()
