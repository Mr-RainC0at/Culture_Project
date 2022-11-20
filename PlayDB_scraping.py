# selenium module 활용하여 자료를 추출

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller

from culture_class import CultureClass, CultureClasses


def playDB_detail_url(onclick_value):
    detail_num = onclick_value.split('\'')[1]
    return 'https://www.playdb.co.kr/playdb/playdbDetail.asp?sReqPlayno=' + detail_num


chromedriver_autoinstaller.install()

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)


def playDB_scraper(url):
    driver.get(url)
    all_pages = 0

    for n in driver.find_elements(By.XPATH,
                                  '//*[@id="contents"]/div[2]/table/tbody/tr[8]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/a[1]/b/font'):  # 제목
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="contents"]/div[2]/table/tbody/tr[8]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/a[1]/b/font')))
        print(n.text)
        all_pages += int(int(n.text[n.text.find("(") + 1:n.text.find(")")]) / 15) + 1

    for page in range(all_pages):
        try:
            links = []

            url = url[0:51] + str(page + 1) + url[52:]
            # print(page+1)
            print(url)
            driver.get(url)

            for t in driver.find_elements(By.CSS_SELECTOR, 'a[onclick]')[1:]:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[onclick]')))
                detailNum = t.get_attribute('onclick')
                # print(playDB_detail_url(detailNum))
                links.append(playDB_detail_url(detailNum))

            for k in links:
                driver.get(k)
                elements = [""] * 9
                for n in driver.find_elements(By.XPATH,
                                              '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[2]/a[1]'):  # 종류
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[2]/a[1]')))
                    # print("제목  " + n.text)
                    elements[0] = n.text

                for n in driver.find_elements(By.XPATH,
                                              '//*[@id="wrap"]/div[3]/div[1]/div[1]/table/tbody/tr[1]/td/span[1]'):  # 제목
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[1]/table/tbody/tr[1]/td/span[1]')))
                    # print("제목  " + n.text)
                    elements[1] = n.text
                # driver.refresh()

                for n in driver.find_elements(By.XPATH,
                                              '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[3]/td[2]/a'):  # 장소
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[3]/td[2]/a')))
                    # print("장소  " + n.text)
                    elements[2] = n.text
                # driver.refresh()

                for n in driver.find_elements(By.XPATH,
                                              '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]'):  # 날짜
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')))
                    # print("날짜  " + n.text)
                    elements[3] = n.text
                # driver.refresh()

                cast = []

                for n in driver.find_elements(By.CSS_SELECTOR, 'a[target=_parent]'):  # 출연진
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[target=_parent]')))
                    # print(n.text)
                    cast.append(n.text)
                elements[4] = cast
                # driver.refresh()

                for n in driver.find_elements(By.XPATH,
                                              '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[2]'):  # 관람 등급
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[2]')))
                    # print("등급  "+ n.text)
                    if n.text[2:3].find("분") != -1:
                        elements[6] = n.text
                    else:
                        elements[5] = n.text
                # driver.refresh()

                for n in driver.find_elements(By.XPATH,
                                              '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[6]/td[2]'):  # 관람 시간
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[6]/td[2]')))
                    # print("시간  " + n.text)
                    if index_in_list(elements, 6):
                        elements[6] = n.text
                # driver.refresh()

                for n in driver.find_elements(By.XPATH,
                                              '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[7]/td[2]/a'):  # 사이트
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/table/tbody/tr[7]/td[2]/a')))
                    # print("사이트  " + n.text)
                    # elements.append(n.text)
                # driver.refresh()

                for n in driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/p/a'):  # 예매 사이트
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[3]/div[1]/div[2]/p/a')))
                    # print("사이트2  " + n.get_property('href'))
                    elements[7] = n.get_property('href')
                # driver.refresh()

                for n in driver.find_elements(By.XPATH, '//*[@id="DivBasic"]/div/div[1]/p'):  # 작품 설명
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="DivBasic"]/div/div[1]/p')))
                    # print("설명  " + n.text)
                    if n.text is not None:
                        elements[8] = n.text
                # driver.refresh()

                [print(el) for el in elements]
                print("---------------------------------------------------------------------------------------------")

                temp_class = CultureClass("PlayDB " + k[-6:], None)
                temp_class.eventType = elements[0]
                temp_class.eventName = elements[1]
                temp_class.location = elements[2]

                date1, date2 = elements[3].split(" ~ ")

                temp_class.eventStartDate = date1.replace("/", "-")
                temp_class.eventEndDate = date2.replace("/", "-")

                temp_class.cast = elements[4]
                temp_class.age = elements[5]
                temp_class.duration = elements[6]
                temp_class.webpage = elements[7]
                temp_class.information = elements[8]
                temp_class.price = "링크 참조"

                CultureClasses.append(temp_class)

        except NoSuchElementException:
            pass

    print("end")


def index_in_list(a_list, index):
    return index < len(a_list)
