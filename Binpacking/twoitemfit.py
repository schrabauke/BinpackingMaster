__author__ = 'Schrabauke'
class BreakIt(Exception): pass

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
