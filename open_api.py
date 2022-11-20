import requests
import json
import datetime
from culture_class import *


# 공공 데이터 포털에서 OpenApi 활용하여 정보 추출:

# 공공 데이터 포털에서 제공하는 OpenApi 자료를 활용하여 CultureClasses에 새로운 문화 생활 객체를 추가하는 함수:
def api_extract(dataName, url):
    page = 1  # 각 OpenApi URL에서 자료를 불러 내는 경우 한 페이지 당 100개의 항목 호출 -> page = 페이지 번호, 1 페이지 부터 검색
    while True:  # 제공된 자료 전부 검색하기 위해 반복문 사용 -> IndexError 발생 전까지 무한 반복 위해 while문 사용
        try:
            # URL의 페이지 번호를 가변 변수 'page'로 변경:
            d = url.find('&pageNo=') + 8
            response = requests.get((str(url[0:d] + str(page) + url[d + 1:])).replace("&type=xml", "&type=json"))

            # 주어진 OpenApi URL에서 json 자료 불러내기(json 모듈 사용):
            json_data = json.loads(response.text, strict=False)

            # json 자료 = 중첩 딕셔너리 형태; 그 중 'items' 키에 해당하는 리스트 추출(리스트 내용 = 개별 딕셔너리)
            # items[n] 예시: {'fcltyNm': '만봉불화박물관', 'fcltyType': '사립', 'rdnmadr': '강원도 영월군 김삿갓면 망경대산길135-3', ...}:
            body = json_data['response']['body']['items']
        except KeyError:  # json 자료에서 dict 형태의 항목 불러내는 중에 발생할 수 있는 KeyError(키 지정 오류) 시 while 반복문 종료
            break
        else:
            for x in range(100):  # 한 페이지(100개 항목)의 항목 검색 위해 for 반복문 사용
                try:
                    CultureClasses.append(CultureClass(name=dataName + ' ' + str(100 * (page - 1) + x),
                                                       p=body[x]))
                except IndexError:  # 항목 개수를 초과하여 반복문을 진행하는 경우 while 반복문 종료
                    break
                print(dataName)
            page = page + 1  # 다음 페이지 넘어가기 위해 page 값 증가, while 반복문 지속


# 행사의 종료 날짜가 지난 경우 CultureClass 객체를 삭제하는 함수:
def remove_past_event(parameter):
    for n in reversed(CultureClasses):  # 함수 삭제시 index 검색에 영향이 없도록 역순으로 index 검색
        if hasattr(n, parameter):  # 입력한 파라미터를 객체가 보유하고 있는지 확인
            # 'yyyy-mm-dd' 형태의 string에서 datetime 모듈 사용, 현재 날짜와 비교하여 날짜가 지난 경우 class 객체 삭제:
            y1, m1, d1 = getattr(n, parameter).split('-')
            if datetime.date(int(y1), int(m1), int(d1)) < datetime.date.today():
                CultureClasses.remove(n)
