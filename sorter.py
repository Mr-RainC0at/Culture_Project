import pickle

fileObj = open('data.obj', 'rb')
exampleObj = pickle.load(fileObj)
fileObj.close()
[print(i.name) for i in exampleObj]
