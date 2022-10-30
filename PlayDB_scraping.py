# https://nureechoi2200.wordpress.com/2020/06/24/playdb-%ED%81%AC%EB%A1%A4%EB%A7%81-playdb%EC%97%90-%EC%98%AC%EB%9D%BC%EC%99%80%EC%9E%88%EB%8A%94-%EA%B3%B5%EC%97%B0-id%EB%A5%BC-%EC%A0%80%EC%9E%A5%ED%95%B4%EB%B3%B4%EC%9E%90-1/
# https://riucc.tistory.com/372
# https://riucc.tistory.com/373?category=743461

# selenium module 활용하여 자료를 추출

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
from data import playDB_url
import time


def playDB_detail_url(onclick_value):
    detail_num = onclick_value.split('\'')[1]
    return 'https://www.playdb.co.kr/playdb/playdbDetail.asp?sReqPlayno=' + detail_num


chromedriver_autoinstaller.install()

options = Options()
options.headless = False

driver = webdriver.Chrome(options=options)
driver.get(playDB_url['playDB_musical_url'][0])

for t in driver.find_elements(By.CSS_SELECTOR, 'a[onclick]')[1:]:
    detailNum = t.get_attribute('onclick')
    print(detailNum)
    print(playDB_detail_url(detailNum))
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[onclick]')))

    driver.get(playDB_detail_url(detailNum))
    for n in driver.find_elements(By.CSS_SELECTOR, 'a[target=_parent]'):
        print(n.text)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[target=_parent]')))

