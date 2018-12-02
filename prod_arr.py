# Creating a new array from the given one such that element at i is product of all elments except i
# use of Division is not allowed
# eg: [1,2,3,4,5]--> [120,60,40,30,24]
# eg: [3,2,1]--> [2,3,6]
# eg: [10,3,5,6,2]--> [180,600,360,300,900]

def prod_arr(arr):
    lst = [1]*len(arr)
    temp = 1
    for i in range(len(arr)):  # Products below the current index
        lst[i] = temp
        temp *= arr[i]
    temp = 1
    for i in range(len(arr)-1, -1, -1): # Products above the current index
        lst[i] *= temp
        temp *= arr[i]
    print(lst)

prod_arr([10,3,5,6,2])