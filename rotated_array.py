# Suppose a sorted array A is rotated at some pivot unknown to you beforehand. eg: 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2

def findMin(A):
    if len(A) == 1:
        return A[0]
    if A[0] < A[-1]:
        return A[0]
    start, end = 0, len(A)-1

    while start <= end:
        mid = (start + end) // 2
        if A[start] > A[mid]:
            if A[mid-1] > A[mid]:
                return A[mid]
            end = mid - 1
        else:
            if A[mid] > A[mid+1]:
                return A[mid+1]
            start = mid + 1
    return -1

print(findMin([4,5,6,7,8,0,1,2,3]))
print(findMin([100,1000,1010,1050,-1,1,2,3]))