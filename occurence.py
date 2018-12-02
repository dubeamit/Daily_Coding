# finding the first and last occurence of a no. in a shorted array
def occurence(A,B,first_occur):
    '''param A--> Array. B--> integer to be searched. boolean first_occur flag'''
    n = len(A)
    low, high = 0, n-1
    result = -1
    while low<=high:
        mid = (low+high) // 2
        if B == A[mid]:
            result = mid
            if first_occur:
                high = mid-1
            else:
                low = mid+1
        elif B < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result

def driver_code(A,B):
    first = occurence(A,B,True)
    last = occurence(A,B,False)
    print("First and Last Occurence are:",first, last)

driver_code([1,2,3,4,4,4,5,6,7],4)