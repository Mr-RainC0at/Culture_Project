# https://nureechoi2200.wordpress.com/2020/06/24/playdb-%ED%81%AC%EB%A1%A4%EB%A7%81-playdb%EC%97%90-%EC%98%AC%EB%9D%BC%EC%99%80%EC%9E%88%EB%8A%94-%EA%B3%B5%EC%97%B0-id%EB%A5%BC-%EC%A0%80%EC%9E%A5%ED%95%B4%EB%B3%B4%EC%9E%90-1/
# https://riucc.tistory.com/372
# https://riucc.tistory.com/373?category=743461

# selenium module을 활용하여 자료를 추출

import csv
from selenium import webdriver

driver = webdriver.Chrome()



def playDB_detail_url(detail_num):
    return 'http://www.playdb.co.kr/playdb/playdbDetail.asp?sReqPlayno=' + detail_num


# driver.get(url)


xpath_default='/html/body/div[1]/div[2]/div[2]/table/tbody/tr[9]/td/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td[3]/table/tbody/tr[1]/td/b/font/a'
