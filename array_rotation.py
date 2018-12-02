# cyclically rotate an array by one
def array_rotation(arr):
    last_elem = arr[len(arr)-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last_elem
    return arr
    
print(array_rotation([1,2,3,4,5,6]))