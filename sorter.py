import pickle
import datetime


def main():
    fileObj = open('data.obj', 'rb')
    AllCultureClasses = pickle.load(fileObj)
    fileObj.close()
    [print(i.name + " " + i.eventStartDate) for i in AllCultureClasses]

    for n in AllCultureClasses:
        if hasattr(n, "fstvlStartDate"):
            n.eventStartDate = n.fstvlStartDate
        if hasattr(n, "fstvlEndDate"):
            n.eventEndDate = n.fstvlEndDate

        def SetEventName(a):
            if hasattr(n, a):
                n.eventName = getattr(n, a)

        SetEventName("fcltyNm")
        SetEventName("eventNm")
        SetEventName("fstvlNm")
        SetEventName("rcrfrstNm")
        SetEventName("sttreeStretNm")
        SetEventName("trrsrtNm")
        SetEventName("LBRRY_NM")
        SetEventName("relicsNm")

        if hasattr(n, "opar"):
            n.location = n.opar
        if hasattr(n, "startLatitude"):
            n.latitude = n.startLatitude
        if hasattr(n, "startLongitude"):
            n.longitude = n.startLongitude

    # 오늘 시작한 객체를 리스트에 저장
    recent = []
    for n in AllCultureClasses:
        y1, m1, d1 = str(getattr(n, "eventStartDate")).split("-")
        if datetime.date(int(y1), int(m1), int(d1)) == datetime.date.today():
            recent.append(n)

    fileObj = open('recent.obj', 'wb')
    pickle.dump(recent, fileObj)
    fileObj.close()

    # 오늘 영업하는 객체를 리스트에 저장
    isOpen = []
    for n in AllCultureClasses:
        y1, m1, d1 = str(getattr(n, "eventStartDate")).split("-")
        try:
            y2, m2, d2 = str(getattr(n, "eventEndDate")).split("-")
        except ValueError:
            pass
        if datetime.date(int(y1), int(m1), int(d1)) <= datetime.date.today() <= datetime.date(int(y2), int(m2),
                                                                                              int(d2)):
            isOpen.append(n)

    fileObj = open('isOpen.obj', 'wb')
    pickle.dump(isOpen, fileObj)
    fileObj.close()


if __name__ == '__main__':
    main()
