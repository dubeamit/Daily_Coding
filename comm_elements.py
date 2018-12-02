# FIND THE COMMON ELEMENTS IN TWO Sorted LIST/ARRAY
def comm_elements(arr1, arr2):
    lst = []
    i,j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            lst.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            i += 1
    return lst

print(comm_elements([1,2,3,4,7,8,9,10],[1,4,5,6,7,8,10]))
print(comm_elements([11,12,14,15,16,17],[12,14,15,17,18]))