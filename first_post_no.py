# Given an unsorted integer array, find the first missing positive integer.
# Example:
# Given [1,2,0] return 3,
# [3,4,-1,1] return 2,
# [-8, -7, -6] returns 1
# Your algorithm should run in O(n) time and use constant space.

def first_post_no(A):
    res = 1
    A = set(a for a in A if a>0)
    while res in A:
        res += 1
    return res

print(first_post_no([1,2,0]))
print(first_post_no([-8, -7, -6]))
print(first_post_no([3,4,-1,1]))