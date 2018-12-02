# Given an array A of integers, find the maximum of j - i 
# subjected to the constraint of A[i] <= A[j].
# A : [3 5 4 2] => 2 for the pair (3, 4)

def max_dist(A):
    n = len(A)
    LMin = [0] * n
    RMax = [0] * n
    LMin[0] = A[0]
    RMax[n-1] = A[n-1]
    for i in range(1,n):
        LMin[i] = min(A[i],LMin[i-1])
    for j in range(n-2, -1, -1):
        RMax[j] = max(A[j],RMax[j+1])
    i, j = 0,0
    max_diff = 0
    while(j<n and i<n):
        if LMin[i] <= RMax[j]:
            max_diff = max(max_diff, j-i)
            j += 1
        else:
            i += 1
    return max_diff

print(max_dist([11,5,6,9,0,15,8,7]))