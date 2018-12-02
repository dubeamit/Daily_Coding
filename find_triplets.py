# Find all triplets with sum equal to zero
def find_triplet(arr, n):
    found = False
    arr.sort()
    for i in range(n-1):
        left = i + 1
        right = n - 1
        cur_elem = arr[i]
        while left < right:
            if (arr[left] + cur_elem + arr[right] == 0):
                print(arr[left], cur_elem, arr[right], end = '     ')
                found = True
                left += 1
                right -= 1
            elif arr[left] + cur_elem + arr[right] < 0:
                left += 1
            else:
                right -= 1
    if found == False:
        print('No triplets of sum zero found')
    print()

find_triplet([0,-1,2,-3,1],5)
find_triplet([1,-2,1,0,5],5)
find_triplet([1,2,7,8,5,3],6)