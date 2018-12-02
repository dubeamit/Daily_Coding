def plus_one(arr):
    carry = 1
    for i in range(len(arr),0,-1):
        carry = carry + arr[i-1]
        borrow = carry//10
        if borrow == 0:
            arr[i-1] = carry
            break
        else:
            arr[i-1] = carry % 10
            carry = borrow
    arr = [borrow] + arr
    while arr[0] == 0:
        del arr[0]
    return arr

print(plus_one([1,9,0]))
print(plus_one([0,0,9,0,9,9]))