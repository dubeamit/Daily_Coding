# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing.
# Return A and B.
#Input:[3 1 2 5 3] Output:[3, 4]  A = 3, B = 4

def repeat_missing(arr):
    size = len(arr) + 1
    count = [0] * size
    for val in arr:
        count[val] += 1
    num1,num2 = 0, 0
    for idx, val in enumerate(count):
        if val == 2:
            num1 = idx
        if val == 0:
            num2 = idx
    return num1, num2

print(repeat_missing([3,1,2,5,1]))