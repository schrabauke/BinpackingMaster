import pdb
from Binpacking.oneitemfit import oneitemfit
from Binpacking.threeitemfit import threeitemfit
from Binpacking.twoitemfit import twoitemfit

__author__ = 'Schrabauke'
from Binpacking.bin import Bin


class BreakIt(Exception): pass

# Uses

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
    while sum(values) >= (maxValue /3):
        print("Beginn of the loop")
        bin = Bin()
        index_1 = 0
        bin.append(values.pop(index_1))
        if bin.sum <= (maxValue / 3):
            for item in values:
                # print(item)
                if bin.sum + item > (maxValue / 3) and bin.sum + item <= maxValue:
                    bin.append(item)
                    values.remove(item)
                    break
        # Step 2: fill the bin with 1, 2 or 3 items plus waste if needed
        else:
            print ( "Start the helperfunction ")
            #  bin = Bin()
            waste = 0;
            while bin.sum != maxValue or waste < maxValue:
                print("Waste ", waste)
                if (oneitemfit(waste, values, maxValue, bin, bins) == True):
                    break;
                elif (twoitemfit(waste, values, maxValue, bin, bins) == True):
                    break;
                elif (threeitemfit(waste, values, maxValue, bin, bins) == True):
                    break
                else:
                    waste += 1;
    else:
        if len(values) == 0:
            return bins
        else:
            bin = Bin()
            for item in values:
                bin.append(item)
        return bins