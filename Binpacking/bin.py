from spyderlib.utils.encoding import writelines

__author__ = 'Bernd'

''' Partition a list into sublists whose sums don't exceed a maximum
    using a First Fit Decreasing algorithm. See
    http://www.ams.org/new-in-math/cover/bins1.html
    for a simple description of the method.
'''

# Daten einlesen
'''
lines = open("E:/PythonProjects/Data/N1C1W1_A.BPP").read().split('\n')
inilist = open("E:/PythonProjects/Data/Instancelist.txt").read().split('\n')
inilist2 = open("E:/PythonProjects/Data/Instancelist2.txt").read().split('\n')
data = open("E:/PythonProjects/Data/" + inilist[1] + ".BPP").read().split('\n')
auswertung = open("E:/PythonProjects/Binpacking/ausgabe.txt", "w")
'''
# Data Laptop
# Path C:\Users\Schrabauke\Desktop\PythonProjects\Data


lines = open("C:/Users/Schrabauke/Desktop/PythonProjects/Data/N1C1W1_A.BPP").read().split('\n')
inilist = open("C:/Users/Schrabauke/Desktop/PythonProjects/Data/Instancelist.txt").read().split('\n')
inilist2 = open("C:/Users/Schrabauke/Desktop/PythonProjects/Data/Instancelist2.txt").read().split('\n')
data = open("C:/Users/Schrabauke/Desktop/PythonProjects/Data/" + inilist[1] + ".BPP").read().split('\n')
auswertung = open("C:/Users/Schrabauke/Desktop/PythonProjects/ausgabe.txt", "w")

data = list



def castdata(list):
    i = 0
    for item in list:
        if item == '':
            list.remove(item)
        else:
            list[i] = int(list[i])
            i = i + 1


castdata(lines)
elements = lines.pop(0)
binsize = lines.pop(0)


class Bin(object):
    ''' Container for items that keeps a running sum '''

    def __init__(self):
        self.items = []
        self.sum = 0

    def append(self, item):
        self.items.append(item)
        self.sum += item

    def __str__(self):
        ''' Printable representation '''
        return 'Bin(sum=%d, items=%s)' % (self.sum, str(self.items))


def firstfit(values, maxValue):
    values = sorted(values, reverse=True)
    bins = []

    for item in values:
        # Try to fit item into a bin
        for bin in bins:
            if bin.sum + item <= maxValue:
                # print 'Adding', item, 'to', bin
                bin.append(item)
                break
        else:
            # item didn't fit into any bin, start a new bin
            # print 'Making new bin for', item
            bin = Bin()
            bin.append(item)
            bins.append(bin)

    return bins


def nextfit(values, maxValue):
    values = sorted(values, reverse=True)
    bins = []
    bin = Bin()
    for item in values:
        if bin.sum + item <= maxValue:
            bin.append(item)

        else:
            # item didn't fit into any bin, start a new bin
            # print 'Making new bin for', item
            bin = Bin()
            bin.append(item)
            bins.append(bin)

    return bins


def bestfit(values, maxValue):
    values = sorted(values, reverse=True)
    bins = []

    for item in values:
        restvalue = 0
        smallestrest = maxValue
        # Try to fit item into a bin
        for bin in bins:
            if bin.sum + item <= maxValue:
                restvalue = maxValue - (bin.sum + item)
                if smallestrest >= restvalue:
                    smallestrest = restvalue
                    bintoadd = bin
        if smallestrest != maxValue:
            bintoadd.append(item)
        else:
            # print 'Making new bin for', item
            bin = Bin()
            bin.append(item)
            bins.append(bin)

    return bins


def worstfit(values, maxValue):
    values = sorted(values, reverse=True)
    bins = []

    for item in values:
        restvalue = 0
        bigrest = 0
        # Try to fit item into a bin
        for bin in bins:
            if bin.sum + item <= maxValue:
                restvalue = maxValue - (bin.sum + item)
                if bigrest <= restvalue:
                    bigrest = restvalue
                    bintoadd = bin
        if bigrest != 0:
            bintoadd.append(item)
        else:
            # print 'Making new bin for', item
            bin = Bin()
            bin.append(item)
            bins.append(bin)
    return bins


def work(data):
    castdata(data)
    elements = data.pop(0)
    binsize = data.pop(0)
    packAndShow(data, binsize)


if __name__ == '__main__':
    import random

    def packAndShow(aList, maxValue):
        ''' Pack a list into bins and show the result '''
        # print('List with sum', sum(aList), 'requires at least', (sum(aList) + maxValue - 1) / maxValue, 'bins')

        # bins = bestfit(aList,maxValue)
        # bins = firstpack(aList, maxValue)
        bins = firstfit(aList, maxValue)
        # num = len(bins)
        print(len(bins))
        # auswertung.write('Solution using' + len(bins) + 'bins:' + 'Elements' + elements,)
        # auswertung.write('{:02d}\n'.format(num))
        # for bin in bins:
        #       print(bin)

        #  print


#TODO implement check if max itemsize is smaller the bin capazity
    aList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    packAndShow(lines, binsize)

    packAndShow(aList, 5)
    aList = [random.randint(1, 11) for i in range(100)]
    packAndShow(aList, 11)

    num = 10
    # Test schreiben
    auswertung.write("Test")
    auswertung.write('{:02d}\n'.format(num))
    auswertung.close()

    # Testprogramm
    # auswertung = open("E:/PythonProjects/Binpacking/ausgabe.txt", "w")

    for item in inilist2:
        data = open("E:/PythonProjects/Data/" + item + ".BPP").read().split('\n')
        work(data)

# auswertung.close()

