# Finding the second Largest from a list/Array
# eg: [1,3,4,5,0,2] --> 4
# eg: [2,2,4] --> 2
# eg: [-2,-1] --> -2
# eg: [] or [2] --> None

import sys

def second_largest(lst):
    if len(lst) < 2:
        return None
    large = sec_large = -sys.maxsize -1 # assigning lowest number possible
    for i in range(len(lst)):
        if lst[i] >= large:
            sec_large = large
            large = lst[i]
    return sec_large

sec_large = second_largest([1,3,4,5,0,2])
print("Second Largest Number", sec_large)