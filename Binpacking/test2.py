import math

__author__ = 'Schrabauke'

#Testfile
import glob
from Finch import exactfit

aList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10 , 5 ,4 ,6, 5,8,4, 9]
maxValue = 10

f = open('finch22.txt', 'w')
#test = exactfit(aList, maxValue)

#Test real Data
#dataname= glob.glob("C:/Users/Schrabauke/Desktop/PythonProjects/Data/*")
#data = open(dataname[10]).read().split('\n')

def castdata(list):
    i = 0
    for item in list:
        if item == '':
            list.remove(item)
        else:
            list[i] = int(list[i])
            i = i + 1

tryi = glob.glob("C:/Users/Schrabauke/Desktop/PythonProjects/Data/*")
#for item in tryi: 57, 58 kritische
for x in range(500,722):
    print(tryi[x])
    data = open(tryi[x]).read().split('\n')
    castdata(data)
    elements = data.pop(0)
    binsize = data.pop(0)
    result = exactfit(data,binsize)
    f.write("%s\n" % result)

#exactfit(data, binsize)
#print("ELEMENTS " , elements)
#print("MIN" , sum(data)/binsize)

f.close()

