# -*-coding: utf-8-*-
# -*-coding: euc-kr-*-

api_url = {
    'Festival': 'http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=json',
    'Museum & Art': 'http://api.data.go.kr/openapi/tn_pubr_public_museum_artgr_info_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=json',
    'Show': 'http://api.data.go.kr/openapi/tn_pubr_public_pblprfr_event_info_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=json',
    'City tour': 'http://api.data.go.kr/openapi/tn_pubr_public_city_tour_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=1&numOfRows=100&type=json',
    'Recreational Forest': 'http://api.data.go.kr/openapi/tn_pubr_public_rcrfrst_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=xml',
    'Boulevard': 'http://api.data.go.kr/openapi/tn_pubr_public_sttree_stret_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=xml',
    'Tourist Attraction': 'http://api.data.go.kr/openapi/tn_pubr_public_sttree_stret_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=xml',
    'Relics': 'http://api.data.go.kr/openapi/tn_pubr_public_nvpc_cltur_relics_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=xml',
    'Library': 'http://api.data.go.kr/openapi/tn_pubr_public_lbrry_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=xml',
    # 'City Park': 'http://api.data.go.kr/openapi/tn_pubr_public_cty_park_info_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=xml'
}

playDB_url = {
    'playDB_musical_url': [
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000001&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=2&sStartYear=&sSelectType=1',
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000001&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=3&sStartYear=&sSelectType=1'],
    'playDB_theatre_url': [
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000002&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=2&sStartYear=&sSelectType=1',
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000002&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=3&sStartYear=&sSelectType=1'],
    'playDB_concert_url': [
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000003&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=2&sStartYear=&sSelectType=1',
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000003&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=3&sStartYear=&sSelectType=1'],
    'playDB_dance_url': [
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000004&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=2&sStartYear=&sSelectType=1',
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000004&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=3&sStartYear=&sSelectType=1'],
    'playDB_classic_opera_url': [
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000005&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=2&sStartYear=&sSelectType=1',
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000005&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=3&sStartYear=&sSelectType=1'],
    'playDB_magic_url': [
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000006&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=2&sStartYear=&sSelectType=1',
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000006&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=3&sStartYear=&sSelectType=1'],
    'playDB_traditional_music_url': [
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000007&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=2&sStartYear=&sSelectType=1',
        'http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000007&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=3&sStartYear=&sSelectType=1']
}

etc_class = [
    # 예시(인덱스 순):
    # 0:명칭                    ex) "코카-콜라 x 아르떼뮤지엄 : “DREAMWORLD”"
    # 1:분류                    ex) "팝업" or "미술관" or ...
    # 2:시작일, 3:종료일         ex) "2022-10-22", "2022-12-04"
    # 4:도로명주소               ex) "서울특별시 마포구 양화로 176 와이즈파크 B2"
    # 5:평일개장시간, 6:평일종료시간, 7:주말개장시간, 8:주말종료시간    ex) "11:00", "20:00", "11:00",  "19:30"
    # 9:가격 (성인 기준)         ex) "0" or "성인 10000원\n 청소년/유아 5000원" or ...
    # 10:소개란                 ex)  홈페이지/인스타 게시글의 내용 복사하여 입력하기(꼭 주최자가 올린 내용일 것):
    # 11:홈피/예매 url          ex) "https://m.booking.naver.com/booking/12/bizes/777722"
    # 12:기타 속성 지정("attr: value")   ex) "fridayEndTime: 19:30" or "mondayStartTime: X" <-- 월요일 휴무 의미

    [
        "코카-콜라 x 아르떼뮤지엄 : \"DREAMWORLD\"",
        "팝업",
        "2022-10-22", "2022-12-04",
        "서울특별시 마포구 양화로 176 와이즈파크 B2",
        "11:00", "20:00", "11:00", "19:30",
        "0",
        """
        코카-콜라 크리에디션 그 세번째 이야기

        무한한 상상력, 꿈의 세계에서 만나요!
        코카-콜라 제로 드림월드 팝업 아트 존에서는 아르떼뮤지엄(ARTE MUSEUM) 작품 중 이번 테마에 어울리는 3개의 작품을 큐레이션 하여 선보입니다. 특히 코카-콜라와의 컬래버레이션을 기념하여 제작한 THUNDER는 드림월드에서 처음 만나보실 수 있습니다.
        
        코카-콜라 크리에디션은 다양한 상상력을 바탕으로 새로운 브랜드 경험을 창조하는 코카-콜라의 글로벌 혁신 프로젝트입니다. 코카-콜라 크리에디션의 세 번째 프로젝트인 코카-콜라 제로 드림월드는 무한한 상상과 가능성이 열려 있는 꿈의 세계에서 영감을 얻어 탄생했습니다. 꿈나라맛을 담아낸 코카-콜라 제로 드림월드는 초현실적이고 환상적인 꿈의 세계가 현실 속에서 펼쳐지는 경험을 통해 일상이 마법같이 짜릿해지는 이색 즐거움을 선사하고자 합니다.
        """,
        "https://m.booking.naver.com/booking/12/bizes/777722",
        "mondayStartTime: X"
    ]

]

# print(etc_class_list[0][12])
