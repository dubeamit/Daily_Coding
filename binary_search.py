def binary_search(arr,key):
    if len(arr)< 1:
        print("Element not found")
        return
    else:
        mid = len(arr)//2
        if key == arr[mid]:
            print("Element found")
        elif key < arr[mid]:
            binary_search(arr[:mid],key)
        elif key > arr[mid]:
            binary_search(arr[mid:],key)

binary_search([1,2,3,4,5,6,7,8,9,10],10)