__author__ = 'Schrabauke'
class BreakIt(Exception): pass

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
