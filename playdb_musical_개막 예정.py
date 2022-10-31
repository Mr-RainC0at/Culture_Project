from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
from data import playDB_url


def playDB_detail_url(onclick_value):
    detail_num = onclick_value.split('\'')[1]
    return 'https://www.playdb.co.kr/playdb/playdbDetail.asp?sReqPlayno=' + detail_num


chromedriver_autoinstaller.install()

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)


for url in playDB_url['playDB_musical_url']:

    driver.get(url)
    all_pages = 0

    for n in driver.find_elements(By.XPATH, '//*[@id="contents"]/div[2]/table/tbody/tr[8]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/a[2]/font'):  # 제목
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[2]/table/tbody/tr[8]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/a[2]/font')))
        print(n.text)
        all_pages += int(int(n.text[n.text.find("(") + 1:n.text.find(")")])/15)+1
    driver.refresh()

    for page in range(1,2):
        try:
            links = []

            url = url[0:52] + str(page) + url[53:]
            print(url)
            driver.get(url)

            for t in driver.find_elements(By.CSS_SELECTOR, 'a[onclick]')[1:]:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[onclick]')))
                detailNum = t.get_attribute('onclick')
                print(detailNum)
                print(playDB_detail_url(detailNum))

                links.append(playDB_detail_url(detailNum))

            for k in links:
                driver.get(k)
                for n in driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[1]/table/tbody/tr[1]/td/span[1]'):  # 제목
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[1]/table/tbody/tr[1]/td/span[1]')))
                    print('제목 : ', n.text)
                driver.refresh()

                for n in driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[3]/td[2]/a'):  # 장소
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[3]/td[2]/a')))
                    print('장소 : ', n.text)
                driver.refresh()

                for n in driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]'):  # 날짜
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')))
                    print('날짜 ; ', n.text)
                driver.refresh()

                for n in driver.find_elements(By.CSS_SELECTOR, 'a[target=_parent]'):  # 출연진
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[target=_parent]')))
                    print('출연진 : ', n.text)
                driver.refresh()

                for n in driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[2]'):  # 관람 등급
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[2]')))
                    print('관람 등급 : ', n.text)
                driver.refresh()

                for n in driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[6]/td[2]'):  # 진행 시간
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[6]/td[2]')))
                    print('진행 시간 : ', n.text)
                driver.refresh()

                for n in driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[7]/td[2]/a'):  # 사이트
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[7]/td[2]/a')))
                    print('사이트 주소 : ', n.text)
                driver.refresh()

                for n in driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/p/a'):  # 예매 사이트
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/p/a')))
                    print('예매 정보 : ', n.get_property('href'))
                driver.refresh()

                print("---------------------------------------------------------------------------------------------")
        except NoSuchElementException:
            pass

print("close")
driver.close()
