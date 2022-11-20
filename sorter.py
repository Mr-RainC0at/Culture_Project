import pickle

fileObj = open('data.obj', 'rb')
CultureClasses = pickle.load(fileObj)
fileObj.close()
[print(i.name + " " + i.eventStartDate) for i in CultureClasses]
