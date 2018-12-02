# Given a sorted array of integers, find the number of 
# occurrences of a given target value.
# Your algorithm’s runtime complexity must be in the order of 
# O(log n).If the target is not found in the array, return 0

def find_count(A,B):
    first_index = binary_search(A,len(A),B,True)
    if first_index == -1:
        return 0
    last_index = binary_search(A,len(A),B,False)
    return (last_index - first_index + 1)

def binary_search(A,n,B,first):
    low, high, result = 0, n-1, -1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == B:
            result = mid
            if first:
                high = mid - 1
            else:
                low = mid + 1
        elif B < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result

print(find_count([5,7,7,8,8,10],8))
print(find_count([1,2,3,4,5,6,7,8,10,10,10,10],10))