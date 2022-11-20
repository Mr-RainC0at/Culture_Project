# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

import data  # Url 등의 데이터 자료를 저장한 파이썬 파일
from instagram_scraping import instagram_extract
from open_api import *
from PlayDB_scraping import *

import pickle


# 프로그램 실행
def main():
    # ----------------------------------------------------------------------------------------------------------------
    # data 파일의 api_url_dict 속 개별 URL에 대해 api_extract 함수 실행 -> CultureClass 객체로 저장
    '''[api_extract(n, u) for n, u in data.api_url_dict.items()]

    remove_past_event('fstvlEndDate')  # 축제 행사 관련, 종료 날짜가 지난 행사 삭제
    remove_past_event('eventEndDate')  # 공연 행사 관련, 종료 날짜가 지난 행사 삭제

    # ----------------------------------------------------------------------------------------------------------------
    # 플레이DB에서 추출한 각종 문화 활동 정보를 CultureClass 객체로 저장
    for u in playDB_url:
            playDB_scraper(u)
'''
    # ----------------------------------------------------------------------------------------------------------------
    # data.py에 직접 입력한 etc_class_list 속 문화 활동 리스트를 CultureClass 객체로 저장
    instagram_extract(data.etc_class_list)

    # ----------------------------------------------------------------------------------------------------------------
    # CultureClasses 리스트를 pickle 모듈을 이용하여 영구적으로 저장

    fileObj = open('data.obj', 'wb')
    pickle.dump(CultureClasses, fileObj)
    fileObj.close()


if __name__ == '__main__':
    main()
