from Binpacking.bin import Bin

__author__ = 'Schrabauke'
"""
Let lst denote the list of items to be bin-packed, let x denote the size of
    the smallest element in lst, and let cap denote the capacity of one bin.
    lst is split into the four sub-lists, lA, lB, lC, lD.
    lA: All items strictly larger than cap/2.
    lB: All items of size at most cap/2 and strictly larger than cap/3.
    lC: All items of size at most cap/3 and strictly larger than (cap - x)/5.
    lD: The rest, i.e., all items of size at most (cap - x)/5.
    Items are placed as follows:
    1. Create a list of length lA bins. Place each item in lA into its own
       bin (while maintaining relative item order with respect to lst).
       Note: relevant published analysis assumes that lst is sorted in order of
       decreasing size.
    2. Take the list of bins created in Step 1 and reverse it.
    3. Sequentially consider each bin b. If the two smallest items in lC do NOT
       fit together into b of if there a less than two items remaining in lC,
       then pack nothing into b and move on to the next bin (if any). If they do
       fit together, then find the largest item x1 in lC that would fit together
       with the smallest item in lC into b. Remove x1 from lC. Then find the
       largest item x2, x2 != x1, in lC that will now fit into b together with
       x1. Remove x2 from lC. Place both x1 and x2 into b and move on to the
       next item.
    4. Reverse the list of bins again.
    5. Use the FirstFit heuristic to place all remaining items, i.e., lB, lD,
       and any remaining items of lC.

       -> Test with aList = [10, 9, 8, 7, 6, 5, 4, 3, 2,2,1]
"""


def modfirstfit(values, maxValue):
    values = sorted(values, reverse=True)
    small_item = values[-1:][0]
    bins = []
    list_a = []
    list_c = []
    index_item = 0
    # Preprocessing of the items in subgroups

    # Step 1 and 2
    while index_item < len(values):
        size_item = values[index_item]
        if size_item > maxValue:
            print("DoesNotFitWarning" + (values[index_item]))
            index_item += 1
            continue

        elif size_item > maxValue / 2:
            list_a.append([values.pop(index_item)])
            continue

        elif (size_item <= maxValue / 3 and size_item > ((maxValue - small_item) / 5)):
            list_c.append(values.pop(index_item))
            continue

        else:
            index_item += 1

    index_a = 0
    #sort the list according to the algorithm
    list_a = sorted(list_a)
    list_c = sorted(list_c)
    # Step 3:
    while index_a < len(list_a):
        # `while` used (over `for`), as list is being modified during iteration.
        try:
            item_a = list_a[index_a][0]
            size_a = item_a

            index_c1 = 0
            item_c1 = list_c[index_c1]  # may raise IndexError
            size_c1 = item_c1

            index_c2 = 1
            item_c2 = list_c[index_c2]  # may raise IndexError
            size_c2 = item_c2

            if sum((size_c1, size_c2, size_a)) > maxValue:
                break  # These are the smallest values, as this is
                # a sorted list. No need to `index_a += 1 ; continue`
        except IndexError:
            index_a += 1
            continue  # next item_a

        # select new item_c1
        if sum((size_c1, size_c2, size_a)) <= maxValue:
            for index_c1_new, item_c1_new in enumerate(list_c):
                if index_c1_new in (index_c1, index_c2):
                    continue
                size_c1_new = item_c1_new
                if sum((size_c1_new, size_c2, size_a)) > maxValue:
                    break
                index_c1 = index_c1_new
                size_c1 = list_c[index_c1]

        # select new item_c2
        if sum((size_c1, size_c2, size_a)) <= maxValue:
            for index_c2_new, item_c2_new in enumerate(list_c):
                if index_c2_new in (index_c1, index_c2):
                    continue
                size_c2_new = item_c2_new
                if sum((size_c1, size_c2_new, size_a)) > maxValue:
                    break
                index_c2 = index_c2_new
                size_c2 = list_c[index_c2]

        assert index_c1 != index_c2, "Index collision"

        # Remove the larger index first (or it _will_ break)
        if index_c1 >= index_c2:
            item_c1 = list_c.pop(index_c1)
        item_c2 = list_c.pop(index_c2)
        if index_c1 < index_c2:
            item_c1 = list_c.pop(index_c1)

        list_a[index_a] += [item_c1, item_c2]
        index_a += 1

    # Step 4:
    list_a.reverse()

        # Step 5:
    values += list_c
    values = sorted(values, reverse=True)
   # bins.append(list_a)

    # add items from list_a to bins -> Working
    for element in list_a:
        bin = Bin()
        for item in element:
            bin.append(item)
        bins.append(bin)


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