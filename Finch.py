__author__ = 'Schrabauke'


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


class BreakIt(Exception): pass

"""
0. Sort the items decreasing
1. Take a new bin and fill it with elements until the bin is over 1/3 full.
2. Try to fill the rest of the bin exactly with single element or combination of the two or three
elements. ( waste = 0 )
3. If there is no such combination that will fill bin exactly, relax the problem with decreasing
the bin size for one (waste =+ 1) and repeat procedure 2 until success.
4. Repeat the whole procedure while there are unassigned elements available.
"""

def exactfit(values, maxValue):
    # ##### Step 0: ######
    values = sorted(values, reverse=True)
    bins = []
    while sum(values) >= (maxValue) :
       # print("Beginn of the loop")
        bin = Bin()
        index_1 = 0
        bin.append(values.pop(index_1))
        if bin.sum == maxValue:
            bins.append(bin)
            alreadyinn = True
        while bin.sum <= (maxValue / 2):
            for item in values:
                # print(item)
                if bin.sum + item <= maxValue:     #bin.sum + item > (maxValue / 2) and
                    bin.append(item)
                    values.remove(item)
                    alreadyinn = False
                    break
        # Step 2: fill the bin with 1, 2 or 3 items plus waste if needed
        if bin.sum > maxValue/2 and bin.sum < maxValue:
           # print ( "Start the helperfunction ")
            #  bin = Bin()
           if min(values) > (maxValue-bin.sum):
                alreadyinn = True
                bins.append(bin)
           else:
                waste = 0;
                while bin.sum != maxValue and waste < maxValue:
                  #  print("Waste ", waste)
                    if (oneitemfit(waste, values, maxValue, bin, bins) == True):
                        alreadyinn = True
                        break;
                    elif (twoitemfit(waste, values, maxValue, bin, bins) == True):
                        alreadyinn = True
                        break;
                    elif (threeitemfit(waste, values, maxValue, bin, bins) == True):
                        alreadyinn = True
                        break
                    else:
                        waste += 1;
                if (waste == maxValue):
                    alreadyinn = True
                    bins.append(bin)
        else:
            if alreadyinn == False:
                bins.append(bin)
                alreadyinn = True
    else:
        if len(values) == 0:
            if alreadyinn == False:
                bins.append(bin)
               # for item in bins:
               #     print(item)
            print("ende", len(bins) , " #Bins")
            return len(bins)
        else:
            if alreadyinn == False:
                bins.append(bin)
            bin = Bin()
            for item in values:
                bin.append(item)
            bins.append(bin)
            print("ende", len(bins) , " #Bins" )
           # for item in bins:
           #     print(item)
            return len(bins)

def oneitemfit(waste, values, maxValue, bin, bins):
    try:
        if len(values) <1:
            return False
        index_1 = 0
        while (index_1 <= len(values) - 1):
            #print(index_1)
            item_a = values[index_1]
            if (bin.sum + item_a + waste == maxValue):
              #  print("Sucess with item", item_a, "index", index_1)
                text1 = True
                bin.append(item_a)
                bins.append(bin)
                values.remove(item_a)
                raise BreakIt
            else:
                index_1 = index_1 + 1
                text1 = False
    except BreakIt:
        pass
    return text1

def threeitemfit(waste, values, maxValue, bin, bins):
    try:
        if len(values) <3:
            return False
        else:
            index_1 = 0;
            while (index_1 < len(values) - 1):
                index_2 = index_1 + 1
                while (index_2 <= len(values) - 2):
                    index_3 = index_2 + 1
                    while (index_3 <= len(values) - 1):
                        #  print(index_1, index_2, index_3)
                        item_a = values[index_1]
                        item_b = values[index_2]
                        item_c = values[index_3]
                        if (bin.sum + item_a + item_b + item_c + waste) == maxValue:
                         #   print("Sucess with items ", item_a, item_b, item_c, "index ", index_1, index_2, index_3)
                            text1 = True
                            bin.append(item_a)
                            bin.append(item_b)
                            bin.append(item_c)
                            bins.append(bin)
                            values.remove(item_a)
                            values.remove(item_b)
                            values.remove(item_c)
                            raise BreakIt
                        else:
                            index_3 = index_3 + 1
                            text1 = False
                    index_2 = index_2 + 1
                    # executed if the loop ended normally (no break)
                index_1 = index_1 + 1
    except BreakIt:
        pass
    return text1;

def twoitemfit(waste, values, maxValue, bin, bins):
    try:
        if len(values) <2:
            return False
        else:
            index_1 = 0
            while (index_1 < len(values) - 1):
                index_2 = index_1 + 1
                while (index_2 <= len(values) - 1):
                  #  print(index_1, index_2)
                    item_a = values[index_1]
                    item_b = values[index_2]
                    if (bin.sum + item_a + item_b + waste) == maxValue:
                      #  print("Sucess with items ", item_a, item_b, "index ", index_1, index_2)
                        text1 = True
                        bin.append(item_a)
                        bin.append(item_b)
                        bins.append(bin)
                        values.remove(item_a)
                        values.remove(item_b)
                        raise BreakIt
                    else:
                        index_2 = index_2 + 1
                        text1 = False
                        # executed if the loop ended normally (no break)
                index_1 = index_1 + 1
    except BreakIt:
        pass
    return text1;