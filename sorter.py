import pickle

fileObj = open('data.obj', 'rb')
CultureClasses = pickle.load(fileObj)
fileObj.close()
[print(i.name + " " + i.eventStartDate) for i in CultureClasses]

# 가장 최근에 시작한 객체 20개를 리스트에 저장
recent=[None]*20

for n in CultureClasses:
    for i in range(20):
        if recent[i] < n.eventStartDate