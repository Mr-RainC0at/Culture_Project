#-*-coding: utf-8-*-
#-*-coding: euc-kr-*-

api_url_dict = {
    'Festival': 'http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=json',
    'Museum & Art': 'http://api.data.go.kr/openapi/tn_pubr_public_museum_artgr_info_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=json',
    'Show': 'http://api.data.go.kr/openapi/tn_pubr_public_pblprfr_event_info_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=json',
    'City tour': 'http://api.data.go.kr/openapi/tn_pubr_public_city_tour_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=1&numOfRows=100&type=json',
    'Recreational Forest': 'http://api.data.go.kr/openapi/tn_pubr_public_rcrfrst_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=xml',
    'Boulevard': 'http://api.data.go.kr/openapi/tn_pubr_public_sttree_stret_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=xml',
    'Tourist Attraction': 'http://api.data.go.kr/openapi/tn_pubr_public_sttree_stret_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=xml',
    'Relics': 'http://api.data.go.kr/openapi/tn_pubr_public_nvpc_cltur_relics_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=xml',
    'Library': 'http://api.data.go.kr/openapi/tn_pubr_public_lbrry_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=xml'
    # 'City Park': 'http://api.data.go.kr/openapi/tn_pubr_public_cty_park_info_api?serviceKey=R8BXy6o1Q5yjiq3dcCId8PVkHF24U99GPcnwOIMKDNzGTCCnEOLDDxSnHPHnKQhHepBZOugew%2F%2BWdMX4EaMLyg%3D%3D&pageNo=0&numOfRows=100&type=xml'
}

playDB_url = [
        'http://www.playdb.co.kr/playdb/playdblist.asp?Page=1&sReqMainCategory=000001&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=2&sStartYear=&sSelectType=1',
        'http://www.playdb.co.kr/playdb/playdblist.asp?Page=1&sReqMainCategory=000002&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=2&sStartYear=&sSelectType=1',
        'http://www.playdb.co.kr/playdb/playdblist.asp?Page=1&sReqMainCategory=000003&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=2&sStartYear=&sSelectType=1',
        'http://www.playdb.co.kr/playdb/playdblist.asp?Page=1&sReqMainCategory=000004&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=2&sStartYear=&sSelectType=1',
        'http://www.playdb.co.kr/playdb/playdblist.asp?Page=1&sReqMainCategory=000005&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=2&sStartYear=&sSelectType=1'
      ]

etc_class_list = [
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
        "11:00", "20:00", "11:00",  "19:30",
        "0",
        """
        코카-콜라 크리에디션 그 세번째 이야기

        무한한 상상력, 꿈의 세계에서 만나요!
        코카-콜라 제로 드림월드 팝업 아트 존에서는 아르떼뮤지엄(ARTE MUSEUM) 작품 중 이번 테마에 어울리는 3개의 작품을 큐레이션 하여 선보입니다. 특히 코카-콜라와의 컬래버레이션을 기념하여 제작한 THUNDER는 드림월드에서 처음 만나보실 수 있습니다.
        
        코카-콜라 크리에디션은 다양한 상상력을 바탕으로 새로운 브랜드 경험을 창조하는 코카-콜라의 글로벌 혁신 프로젝트입니다. 코카-콜라 크리에디션의 세 번째 프로젝트인 코카-콜라 제로 드림월드는 무한한 상상과 가능성이 열려 있는 꿈의 세계에서 영감을 얻어 탄생했습니다. 꿈나라맛을 담아낸 코카-콜라 제로 드림월드는 초현실적이고 환상적인 꿈의 세계가 현실 속에서 펼쳐지는 경험을 통해 일상이 마법같이 짜릿해지는 이색 즐거움을 선사하고자 합니다.
        """,
        "https://m.booking.naver.com/booking/12/bizes/777722",
        "mondayStartTime: X"
    ],

    [
        "LG 금성오락실 in 강남",
        "팝업",
        "2022-10-12", "2022-11-27",
        "서울특별시 강남구 강남대로 420",
        "12:00", "21:00", "11:00",  "20:00",
        "0",
        """
        금성오락실 오픈하는구나, 마침내! 모두 쏴~리 질럿!! 

        금성오락실 강남점 절찬리 오픈!

        더 깊어진 몰입감으로 다양한 게임을 즐기고 싶다면 모두 금성오락실로 놀러와~
        금성오락실의 모든 게임은 무료! 건물 앞 광장, 1층, 2층 전부다~
        LG전자의 신제품, 올레드 FLEX를 체험해볼 수 있는 기회! 오락실 2층 FLEX ARCADE 존으로 고고!
        어서, 지금, 빨리 강남역으로 출발! 강남대로 420, 역삼빌딩에서 영업중~
        """,
        "https://www.instagram.com/p/Cjmy5A1PknD/?utm_source=ig_web_copy_link",
        "mondayStartTime: X"
    ],

    [
        "슬입앤슬립 코디센",
        "팝업",
        "2022-10-07", "2022-12-31",
        "대전광역시 서구 문정로 72",
        "11:00", "20:00", "11:00",  "20:00",
        "0",
        """
        침구 브랜드 이브자리에서 세탁서비스를 제공하는 팝업스토어를 오픈! 

        슬립앤슬립 팝업스토어에서는 경추 측정기 경험과 인생 베개, 토퍼 찾기가 가능~

        이번 겨울 따뜻한 이불 쇼핑하러 슬립앤슬립으로 고고~!
        """,
        "자유입장",
        "mondayStartTime: X"
    ],

    [
        "활명수 125주년 기념 \'활명수 1897\' 팝업스토어 오픈",
        "팝업",
        "2022-10-19", "2022-11-10",
        "서울특별시 성동구 서울숲2길 42",
        "12:00", "21:00", "12:00",  "21:00",
        "0",
        """
        활명수 탄생 및 창립 125주년 기념 팝업스토어 오픈~!

        서울의 유명 핫플레이스인 성수동 서울숲 카페거리에서 진행되는 팝업스토어는 총 5개의 공간으로 구성되어 19세기에서 21세기까지 활명수의 탄생과 역사를 다채롭게 보여준대~!

        또한 동화약품의 예전 제품들과 함께 역대 광고 및 CF 등도 관람할 수 있는 라이브러리까지!
        
        팝업스토어에서 활명수의 히스토리를 관람하고 포토존에서 사진도 찍을 수 있으니 꼭 가보자~
        """,
        "자유입장",
        "mondayStartTime: X"
    ],

    [
        "파이롯트 오피스 : 소중한 말들 모음 사무소",
        "팝업",
        "2022-10-15", "2022-11-27",
        "서울특별시 성수동 연무장길 57",
        "11:00", "20:00", "11:00",  "20:00",
        "0",
        """
        "어서오세요! 파이롯트 오피스입니다!"

        드디어 파이롯트 오피스 <소중한 말들 모음소> 가 오픈했습니다!!

        파이롯트의 상징인 블루컬러로 꾸며진 유머러스한 공간에서 일상의 말, 끄적임을 소중한 기록으로 남겨보세요.
        """,
        "https://www.instagram.com/p/CjaMaotr8Gf/",
        "mondayStartTime: X"
    ],


    [
        "합스부르크 600년, 매혹의 걸작들",
        "미술관",
        "2022-10-25", "2023-03-01",
        "서울특별시 용산구 서빙고로 137 국립중앙박물관",
        "10:00", "18:00", "10:00",  "18:00",
        "성인 17500원 / 청소년 15000원 / 어린이 10000원",
        """
        국립중앙박물관은 한국과 오스트리아 수교 130주년을 기념하여 오스트리아 빈미술사박물관 대표 소장품전을 개최합니다.

        합스부르크 왕가는 13세기 신성로마제국 황제를 배출한 이후 15~20세기 초까지 600여년 간 신성로마제국과 오스트리아 영토를 다스리는 황제로 군림한 가문이며 유럽의 정세에 가장 영향력 있던 명문가 중 하나입니다. 

        이번 전시에서는 15~20세기까지 합스부르크 왕가가 수집한 르네상스, 바로크미술 시기 대표 소장품을 통해 오스트리아의 역사와 문화를 조명하는 회화, 공예, 갑옷, 태피스트리 등 96점의 전시품이 소개됩니다. 피터르 파울 루벤스, 디에고 벨라스케스, 틴토레토, 베로네세, 안토니 반 다이크, 얀 스테인 등 빈미술사박물관 소장 서양미술 거장들의 명화도 직접 만나볼 수 있습니다.

        특히 1892년 수교 당시 고종이 오스트리아 프란츠 요제프 1세에게 선물했던 조선의 갑옷과 투구도 이번 전시에 선보이게 되어, 수교 130주년 기념의 의미도 되새기는 전시가 될 것으로 기대합니다.
        """,
        "https://www.museum.go.kr/site/main/exhiSpecialTheme/view/upcomming?exhiSpThemId=648213&listType=list",
        "mondayStartTime: X"
    ],


    [
        "외규장각 의궤, 그 고귀함의 의미",
        "전시회",
        "2022-11-01", "2023-03-19",
        "서울특별시 용산구 서빙고로 137 국립중앙박물관",
        "10:00", "18:00", "10:00",  "18:00",
        "성인 5000원 / 청소년 3000원 / 어린이 3000원",
        """
        조선왕조의궤는 조선의 정신적 근간이자 500년 역사의 문화 자산입니다. 이제는 세계기록문화유산으로서 그 절대적 가치를 인정받고 있습니다.

        조선왕조의궤 중에서도 왕만 볼 수 있도록 만든 어람용 외규장각 의궤. 프랑스로부터 외규장각 의궤가 돌아 온지 10년이 지났습니다. 

        그동안 의궤 속에서 찾아낸 다양한 이야기들을 모아 여러분께 소개합니다. 

        의식의 궤범軌範’ 의궤는 조선시대의 중요 국가 행사를 처음부터 끝까지, 하나하나 상세하게 기록해놓은 책입니다.
        그 중에서도 외규장각 의궤는 오직 왕 만을 위하여 가장 귀한 재료로 가장 정성스럽게 만든 귀하디귀한 책입니다.
        생김새도 귀하지만 담고 있는 내용은 더욱 귀합니다.
        예법禮法으로 나라를 다스리고 백성들을 이끄는 품격의 통치, 그리로 가는 길이 바로 의궤 속에 있습니다.

        왕의 책, 외규장각 의궤. 그 고귀한 가치를 국립중앙박물관에서 만나보시기 바랍니다.
        """,
        "https://www.museum.go.kr/site/main/exhiSpecialTheme/view/upcomming?exhiSpThemId=946608&listType=list",
        "mondayStartTime: X"
    ],


    [
        "대한제국 첫 궁중 연회",
        "전시회",
        "2022-09-06", "2022-12-25",
        "서울특별시 용산구 서빙고로 137 국립중앙박물관",
        "10:00", "18:00", "10:00",  "18:00",
        "0",
        """
        1901년(신축년) 음력 5월, 대한제국 황실의 어른 효정왕후(헌종의 계비, 명헌태후, 1831-1904)의 71세를 경축하는 궁중 연회 진찬進饌이 경운궁에서 열렸습니다.
        여러 날에 걸쳐 열린 연회 중에서, 다섯 행사의 장면을 그린 병풍을 <신축진찬도辛丑進饌圖>라고 합니다. 
        1897년 대한제국 선포 후 처음으로 열린 궁중 연회를 그린 <신축진찬도>는 황제의 나라 위상에 맞는 기물과 복식 등을 확인할 수 있는 중요한 작품입니다.
        """,
        "https://www.museum.go.kr/site/main/exhiSpecialTheme/view/current?exhiSpThemId=866364&listType=list",
        "mondayStartTime: X"
    ],


    [
        "일본 불교조각의 세계",
        "전시회",
        "2022-04-05", "2023-10-09",
        "서울특별시 용산구 서빙고로 137 국립중앙박물관",
        "10:00", "18:00", "10:00",  "18:00",
        "0",
        """
        이 전시는 일본 도쿄국립박물관 소장의 불교조각품을 특별 공개하는 전시입니다.
        일본의 불교미술은 6세기 이후 다양한 모습으로 발전해왔습니다.
        초기에는 한국과 중국의 영향을 받은 불상을 만들었으나, 헤이안 시대에 해당하는 9세기부터는 일본의 독자적인 불교문화가 나타납니다. 
        대일여래를 중심으로 한 밀교密敎와 아미타여래를 중심으로 한 정토교淨土敎가 대표적입니다. 
        그리고 일본 고유의 신앙과 불교가 합해진 신불습합神佛習合 또한 한국과 중국에서는 없는 일본의 독특한 불교문화입니다. 
        이번 전시에서는 일본의 불교신앙인 밀교, 정토교, 신불습합을 대표하는 5점의 조각품을 선보입니다.

        일본에서 불상은 주로 국가사업이나 귀족, 무사 가문의 후원으로 만들어졌습니다. 
        완성된 불상은 오랜 시간 동안 많은 사람에게 위안과 감동을 주었을 것입니다. 
        불상에 담긴 염원은 시간과 장소를 뛰어넘습니다. 
        어려운 상황에서도 먼 바다를 건너 우리를 찾아온 부처와 만나, 그 염원의 의미와 가치를 되새겨 보시기 바랍니다.
        """,
        "https://www.museum.go.kr/site/main/exhiSpecialTheme/view/current?exhiSpThemId=650312&listType=list",
        "mondayStartTime: X"
    ],


    [
        "영원한 삶의 집, 아스타나 고분",
        "전시회",
        "2022-07-16", "2023-07-15",
        "서울특별시 용산구 서빙고로 137 국립중앙박물관",
        "10:00", "18:00", "10:00",  "18:00",
        "0",
        """
        아스타나[阿斯塔那] 고분은 중국 신장웨이우얼자치구 투루판시에서 동남쪽으로 35km 떨어진 곳으로, 투루판의 옛 도읍인 고창고성(高昌故城) 부근에 있습니다. 
        3세기경부터 8세기 후반까지 만들어진 지배 계층의 공동묘지로 400기가 넘는 무덤이 발견되었습니다. 
        20세기 초 서구 열강이 주도한 실크로드 탐험과 1959년부터 수차례 이루어진 중국 신장박물관의 발굴에서 복희와 여와 그림, 나무와 흙으로 만든 인물상과 토기, 문서 등 상태가 좋은 다양한 부장품이 많이 나왔습니다.

        이번 전시는 그 가운데 국립중앙박물관이 소장한 20세기 초 오타니[大谷] 탐험대의 수집품 중 85점의 아스타나 고분 출토품에 대한 조사 성과를 공개하는 자리입니다. 
        〈명기와 나무 받침〉은 박물관에 들여올 때의 자료에 근거해 한 벌의 구성으로 재현할 수 있었습니다.
       〈말을 탄 무인상〉은 파편들을 접합해 복원했으며, 컴퓨터 단층촬영[CT]으로 제작 방법을 알 수 있었습니다. 

        무덤 속 공간에 맞게 전시된 부장품들은 영원한 삶을 위해 꾸민 아스타나 고분의 특징을 잘 보여줍니다. 
        죽은 뒤에도 현세의 삶이 이어지기를 빌었던 사람들의 염원을 느껴보시기 바랍니다.
        """,
        "https://www.museum.go.kr/site/main/exhiSpecialTheme/view/current?exhiSpThemId=773164&listType=list",
        "mondayStartTime: X"
    ],


    [
        "에릭 루 피아노 리사이틀",
        "음악회",
        "2022-12-06", "2022-12-06",
        "서울특별시 서초구 남부순환로 2406 서울 예술의 전당",
        "00:00", "00:00", "19:30",  "21:30",
        "R석 90000원 / S석 70000원 / A석 50000원",
        """
        2018년 리즈 국제 피아노 콩쿠르 우승자 에릭 루
        피아니스트 에릭 루는 20세의 나이로 2018년 리즈 국제 피아노 콩쿠르에서 1등 상을 차지하며 국제 클래식계에 화려하게 등장했다.
        12월 6일 피아니스트 에릭 루의 연주가 서울 예술의전당에서 열릴 예정이다. 
        """,
        "https://tickets.interpark.com/goods/22008644",
        "mondayStartTime: X"
    ],


    [
        "오마주 투 쇼팽",
        "음악회",
        "2022-12-11", "2022-12-11",
        "서울특별시 서초구 남부순환로 2406 서울 예술의 전당",
        "00:00", "00:00", "17:00",  "19:00",
        "R석 90000원 / S석 70000원 / A석 50000원",
        """
        더벨과 함께하는 오마주 투 쇼팽
        낭만을 그렸던 작곡가 프레데릭 쇼팽, 그에게 바치는 단 한 번의 헌정!
        """,
        "https://tickets.interpark.com/goods/22012854",
        "mondayStartTime: X"
    ],


    [
        "2022 파리나무십자가 소년합창단 특별초청공연",
        "음악회",
        "2022-12-16", "2022-12-16",
        "서울특별시 서초구 남부순환로 2406 서울 예술의 전당",
        "00:00", "00:00", "19:30",  "21:30",
        "R석 110000원 / S석 90000원 / A석 70000원 / B석 50000원 / C석 40000원",
        """
        프랑스의 향기를 가득담다!

        올해 공연의 감상포인트는 프랑스 오페라 발레 작곡가 장 필립 라모의 ‘평화로운 숲(Forets Paisibles)’을 비롯하여 유명 프랑스 작곡가들의 음악을 감상하며 프랑스 음악의 진수와 아름다움을 흠뻑 느껴볼수 있다. 
        또한 비발디, 슈베르트등의 정통클래식곡들, 즐거운 크리스마스 캐롤, 매번 관객의 기립박수를 받는 한국곡들을 앵콜로서 노래하며 한 겨울밤 사랑과 감동이 함께하는 가슴설레이는 잊지못할 성탄 무대를 선사한다.
        """,
        "https://www.sac.or.kr/site/main/show/show_view?SN=49076",
        "mondayStartTime: X"
    ],


    [
        "사라 장 & 비르투오지",
        "음악회",
        "2022-12-16", "2022-12-16",
        "경기도 광주시 회안대로 891 남한산성아트홀",
        "00:00", "00:00", "19:30",  "21:30",
        "R석 100000원 / S석 80000원 / A석 50000원",
        """
        사라 장 & 비르투오지

        슈퍼스타 바이올리니스트 사라 장과 젊은 거장들이 선보이는 화려한 무대!

        2022년 연말을 장식하는 비탈리, 바흐, 비발디 등 아름다운 바로크 음악!
        """,
        "https://www.nsart.or.kr/perform.do?act=detail&pfrmId=281",
        "mondayStartTime: X"
    ],



    [
        "국립합창단 제192회 정기연주회 <2022 송년축하 음악회>",
        "음악회",
        "2022-12-12", "2022-12-12",
        "서울특별시 송파구 올림픽로 300 롯데 콘서트홀",
        "00:00", "00:00", "19:30",  "20:40",
        "R석 50000원 / S석 30000원 / A석 20000원 / B석 10000원",
        """
        국립합창단 제192회 정기연주회 <2022 송년축하 음악회>

        2022년, 저물어가는 한 해를 돌아보고 국립합창단과 함께 다가오는 2023년 희망찬 새해를 맞이하는 특별한 시간!

        국립합창단의 창작 합창곡 및 한국 가곡 그리고 한국인들이 즐겨 부르는 우리 가요 명곡들을 합창 클래식 버전으로 새롭게 편곡하여 선보이는 무대로, 2022년 한 해를 되돌아보고 다가오는 2023년 새해를 맞이하는 시간을 가진다.  

        국립합창단 단장 겸 예술감독 윤의중의 지휘로 소프라노 강혜정, 바리톤 김기훈 그리고 국립합창단이 이번 <2022 송년축하 음악회>에 함께한다.
        """,
        "https://tickets.interpark.com/goods/22014036",
        "mondayStartTime: X"
    ]

]



# print(etc_class_list[0][12])
