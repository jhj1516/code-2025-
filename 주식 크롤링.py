# 먼저 입력하고 시작작
#1. [.\myenv\Scripts\activate]
#2. [python]

import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

#1. 페이지 이동
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)

#2.조회 항목 초기화(체크 해제)
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected(): #체크 된 상태인지 확인
        checkbox.click() #클릭 해서 체크 없애기

#3. 조회 항목 설정
items_to_select = ['영업이익', '자산총계', '매출액']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..') #부모 element
    label = parent.find_element(By.TAG_NAME, 'label')
    if label.text in items_to_select:
        checkbox.click()

#4. 적용하기 버튼 사용
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()

for idx in range(1,40): #1~40 미만 페이지 반복
    #4. 사전 작업 : 페이지 이동
    browser.get(url + str(idx))

    #5. 데이터 추출
    df = pd.read_html(browser.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True)
    df.dropna(axis='columns', how='all', inplace=True)
    if len(df) == 0:
        break
    
    #6. 파일 저장
    f_name = 'sise.csv'
    if os.path.exists(f_name): #파일이 있다면 헤더 부분을 제외
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
    else: # 파일이 없다면 헤더 포함
        df.to_csv(f_name, encoding='utf-8-sig', index=False)
    print(f'{idx} 페이지 완료')

browser.quit()