# You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time 
# and constant additional space. If so, return the integer. If not, return -1.
# If there are multiple solutions, return any one.

def n_by_3_repeated_no(A):
    n = len(A) // 3
    dictionary = {}
    for i in A:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
        for key, value in dictionary.items():
            if value > n:
                return key
    return -1

print(n_by_3_repeated_no([1, 2, 3, 1, 1]))
print(n_by_3_repeated_no([1000441, 1000441, 1000994 ]))