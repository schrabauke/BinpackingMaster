from Binpacking.bin import Bin

__author__ = 'Schrabauke'


class BreakIt(Exception): pass


aList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
values = aList
maxValue = 10
index_1 = 0
index_2 = 0
index_3 = 0


if 1 in aList:
    print ("yes")

test = filter(lambda x : x < 4, aList)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filter(lambda x : x < 4, a)


# Index
#  2 erhöhen und index eins ganz lassen -> eine zwischenschleife mit index_2
# index kann den wert 10 bekommen -> index out of range error
while index_1 < len(values) - 1:
    index_2 = index_1 + 1
    print("Aüßere Schleife index 1 ", index_1)
    print("Äußere Schleife index 2 ", index_2)
    while index_2 <= len(values) - 1:
        print("index bevor erhöhung", index_2, index_1)
        item_a = values[index_1]

        item_b = values[index_2]
        print("items zum checken", item_a, item_b)
        if sum((item_a, item_b)) == maxValue:
            print("Items passen genau rein", item_a, item_b)
            break  # These are the smallest values, as this is
        # a sorted list. No need to `index_a += 1 ; continue`
        elif index_2 != len(values) - 1:
            #
            print("Erhöhe index_2", index_2)
            index_2 += 1
            continue
        else:
            print("Raufhüpfen")
            index_1 += 1
            break


# ###Test with ausgekoppelten versionen
def oneitemfit(waste, values, maxValue, bin, bins):
    try:
        index_1 = 0
        while (index_1 <= len(values) - 1):
            #print(index_1)
            item_a = values[index_1]
            if (bin.sum + item_a + waste == maxValue):
                print("Sucess with item", item_a, "index", index_1)
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


ergebtniss = oneitemfit(0, values, 11, bin, bins)
#######################################################################################
################so gehts :D########################
aList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1,10,9,5,5,7,8,7,6,2,2]
values = aList
maxValue = 10
index_1 = 0
index_2 = 0
index_3 = 0

        bin = Bin()
        index_1 = 0
bins = []

bin = Bin()
waste = 0;
while bin.sum != maxValue or waste == 15:
    print("Waste ", waste)
    if (oneitemfit(waste, values, maxValue, bin, bins) == True):
        break;
    elif (twoitemfit(waste, values, maxValue , bin , bins) == True):
        break;
    elif (threeitemfit(waste, values, maxValue , bin, bins) == True):
        break
    else:
        waste += 1;

test = exactfit(values, maxValue)

# ###Test with ausgekoppelten versionen
def oneitemfit(waste, values, maxValue, bin, bins):
    try:
        index_1 = 0
        while (index_1 <= len(values) - 1):
            #print(index_1)
            item_a = values[index_1]
            if (bin.sum + item_a + waste == maxValue):
                print("Sucess with item", item_a, "index", index_1)
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

def twoitemfit(waste, values, maxValue, bin, bins):
    try:
        index_1 = 0
        while (index_1 < len(values) - 1):
            index_2 = index_1 + 1
            while (index_2 <= len(values) - 1):
                print(index_1, index_2)
                item_a = values[index_1]
                item_b = values[index_2]
                if (bin.sum + item_a + item_b + waste) == maxValue:
                    print("Sucess with items ", item_a, item_b, "index ", index_1, index_2)
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

def threeitemfit(waste, values, maxValue, bin, bins):
    try:
        index_1 = 0;
        while (index_1 < len(values) - 1):
            index_2 = index_1 + 1
            while (index_2 <= len(values) - 2):
                index_3 = index_2 + 1
                while (index_3 <= len(values) - 1):
                    print(index_1, index_2, index_3)
                    item_a = values[index_1]
                    item_b = values[index_2]
                    item_c = values[index_3]
                    if (bin.sum + item_a + item_b + item_c + waste) == maxValue:
                        print("Sucess with items ", item_a, item_b, item_c, "index ", index_1, index_2, index_3)
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

print("index Error", index_2)
index_2 += 1
print("Erhöhe index_1", index_2)
continue  # next item_a

i = 1
while (i < 6 ):
    j = i + 1
    while (j <= 5):
        q = j + 1
        while (q <= 6):
            print(i, j, q)
            q = q + 1
        j = j + 1
    i = i + 1


text1 = False
exactfit(values, maxValue)

test = exactfit(data, binsize)