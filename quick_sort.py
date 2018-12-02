# Quick_Sort
# p-q-1--> elements less than pivot(r)
#q-r --> elements greater than pivot(r)
#j-r-1 --> elements relation yet to be determined with pivot (r)

def quick_sort(arr, p, r):
    if p<r:
        pivot = partition(arr,p,r)
        quick_sort(arr,p,pivot-1)
        quick_sort(arr,pivot+1,r)

def partition(arr, p, r):
    q = p 
    for j in range(p,r):
        if arr[j] <= arr[r]:
            arr[j], arr[q] = arr[q], arr[j]
            q += 1
            j += 1
        else:
            j += 1
    arr[r],arr[q] = arr[q],arr[r]
    return q

arr = [9,7,5,11,12,-2,-1,3,0,4,6]
quick_sort(arr,0,len(arr)-1)
print(arr)