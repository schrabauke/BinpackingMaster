class BreakIt(Exception): pass
__author__ = 'Schrabauke'

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

