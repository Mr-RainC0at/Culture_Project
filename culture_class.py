from geopy.geocoders import Nominatim


class CultureClass:  # 문화 생활 class 정의
    def __init__(self, name, p):
        self.name = name

        # 딕셔너리를 입력하는 경우 딕셔너리의 (키 -> 값) 을 class의 (인스턴스 속성 -> 값)으로 지정:
        if type(p) == dict:
            [setattr(self, k, v) for k, v in p.items()]

        # 리스트를 입력하는 경우 순서에 따라 속성값 부여
        elif type(p) == list:
            self.eventName = p[0]   # 0:명칭
            self.eventType = p[1]   # 1:분류

            self.eventStartDate = p[2]  # 2:시작일, 3:종료일
            self.eventEndDate = p[3]

            self.roadAddress = p[4]     # 4:도로명 주소

            geo_local = Nominatim(user_agent='South Korea')
            try:
                d = p[4].replace("로 ", "길 ").find("길 ") + 1                     # <- 도로명 주소의 상세 주소 제거
                remove_detail = p[4][0:d] + " " + p[4][d+1:].split(" ", 1)[0]     # <-
                geo = geo_local.geocode(remove_detail)  # 도로명 주소에서 위도, 걍도 얻는 geopy 모듈 사용
                self.latitude, self.longitude = [geo.latitude, geo.longitude]   # class에 위도, 경도 속성 부여
            except ValueError:
                # 입력한 도로명 주소에 오류가 있는 경우 위도, 경도 = 성균관대학교 주소
                self.latitude, self.longitude = [126.974304, 37.2936923]
            except AttributeError:
                # 입력한 도로명 주소에 오류가 있는 경우 위도, 경도 = 성균관대학교 주소
                self.latitude, self.longitude = [126.974304, 37.2936923]

            self.weekdayStartTime = p[5]    # 5:평일 개장 시간, 6:평일 종료 시간
            self.weekdayEndTime = p[6]

            self.mondayStartTime = self.weekdayStartTime    # 5, 6에 따라 개별 평일 시간 설정(밑에 수정 가능)
            self.tuesdayStartTime = self.weekdayStartTime
            self.wednesdayStartTime = self.weekdayStartTime
            self.thursdayStartTime = self.weekdayStartTime
            self.fridayStartTime = self.weekdayStartTime

            self.mondayEndTime = self.weekdayEndTime
            self.tuesdayEndTime = self.weekdayEndTime
            self.wednesdayEndTime = self.weekdayEndTime
            self.thursdayEndTime = self.weekdayEndTime
            self.fridayEndTime = self.weekdayEndTime

            self.weekendStartTime = p[7]    # 7:주말 개장 시간, 8:주말 종료 시간
            self.weekendEndTime = p[8]

            self.saturdayStartTime = self.weekendStartTime  # 7, 8에 따라 개별 주말 시간 설정(밑에 수정 가능)
            self.sundayStartTime = self.weekendStartTime

            self.saturdayEndTime = self.weekendEndTime
            self.sundayEndTime = self.weekendEndTime

            if p[9] == '0':     # 9:가격 (성인 기준)
                self.price = '무료'
            else:
                self.price = p[9]

            self.information = p[10]    # 10:소개란
            self.page = p[11]           # 11:홈피/예매 url

            if p[12] is not None:   # 12:기타 속성 지정("attr: value") -> 개별 요일 시간 변경도 가능
                for p in p[14:]:
                    attr, val = p.split(": ")
                    setattr(self, attr, val)


CultureClasses = list()  # 문화 생활 class 수합 list(개별 class 지정 용도)
