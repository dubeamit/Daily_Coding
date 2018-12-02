def rec_prod_arr(arr,prod,i):
    if i < len(arr):
        prod.append(arr[i-1] * prod[i-1]) if i>0 else prod.append(1)
        temp_ret = rec_prod_arr(arr, prod, i+1)
        prod[i] *= temp_ret
        return temp_ret * arr[i]
    return 1

lst = []
rec_prod_arr([3,2,1],lst,0)
print(lst)
