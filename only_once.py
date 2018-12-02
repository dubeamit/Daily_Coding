# Given an array where every element occurs three times, except one element which occurs only once. 
# Find the element that occurs once. Expected time complexity is O(n) and O(1) extra space.
# Input: [12, 1, 12, 3, 12, 1, 1, 2, 3, 3] --> Output: 2
# ( 3*(sum_of_array_without_duplicates) – (sum_of_array) ) / 2

def only_once(arr):
    return (3*sum(set(arr)) -  sum(arr))//2
    # 3 * arr without duplicate ==> thrice the sum of each element of the array
    # sum of arr will give thrice of all no. except single element 
    # subtracting them will give --> remaining no. which on adding the element which appears only once will be 3* the elem
    # hence divide by 2 will give the elem that appears only once.

print("Element that appear only once is",only_once([12, 1, 12, 3, 12, 1, 1, 2, 3, 3]))
print("Element that appear only once is",only_once([12, 1, 12, 12]))