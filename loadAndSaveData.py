from json import dump
from json import loads


def loadAllData() :
    with open('data.txt') as savedData:
        data = savedData.read()
        js = loads(data)

        
    return js[0]

def loadData(dataFile) :
    with open(dataFile) as savedData:
        data = savedData.read()
        js = loads(data)
    return js[0]

def saveData(data, dataFile) :
    savedDataList = []
    savedDataList.append(data)
    savedDataFile = open(dataFile, "w")
    dump(savedDataList, savedDataFile)