# given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1
# Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(asc) that sub array, then the whole array should get sorted.
# If A is already sorted, output -1

def sub_unsorted(A):
    B = sorted(A)
    start, end = 0,0
    for i in range(len(A)):
        if A[i] != B[i]:
            start = i
            break
    for i in range(len(A)-1,-1,-1):
        if A[i] != B[i]:
            end = i
            break
    return [-1] if start==end==0 else [start,end]

print(sub_unsorted([1,3,2,4,5]))
print(sub_unsorted([1,1,2,3,4,4,6,5,7]))