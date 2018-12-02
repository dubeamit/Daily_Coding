# Given an array of integers, sort the array into a wave like array and return it, 
# In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5
# Given [1, 2, 3, 4]
# One possible answer : [2, 1, 4, 3]
# Another possible answer : [4, 1, 3, 2]
# If there are multiple answers possible, return the one thats lexicographically smallest. 
# So, in example case, you will return [2, 1, 4, 3] 


def wave_sort(A):
    A.sort()
    for i in range(0,len(A)-1,2):
        A[i], A[i+1] = A[i+1], A[i]
    return A

print(wave_sort([-1,5,9,0,1,3]))
print(wave_sort([4,1,2,3]))
