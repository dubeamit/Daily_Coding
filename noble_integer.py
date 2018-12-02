# Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the
# array equals to p If such an integer is found return 1 else return -1.
def noble_integer(A):
    n = len(A)
    A.sort()
    for i in range(n-1):
        if A[i] == A[i+1]: # For repeated vaule
            continue 
        if A[i] == n-i-1:
            return A[i]
    if A[n-1] == 0:
        return 0
    return -1

print(noble_integer([5,6,2]))
print(noble_integer([-1, -9, -2, -78, 0]))
print(noble_integer([7, 3, 16, 10]))