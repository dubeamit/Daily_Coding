# GIVEN TWO ARRAY CHECK IF THEY ARE ROTATION OF EACH OTHER
def is_arr_rotated(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    key = arr1[0]
    key_index = -1
    for i in range(len(arr2)):
        if key == arr2[i]:
            key_index = i
            break
    for i in range(len(arr1)):
        j = (key_index+i) % len(arr1)
        if arr1[i] != arr2[j]:
            return False
    return True

print(is_arr_rotated([1,2,3,4,5,6,7],[4,5,6,7,1,2,3]))
print(is_arr_rotated([1,2,3,4,5,6,7],[4,5,6,7,1,2,0]))