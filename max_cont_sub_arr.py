# Find largest sum contiguous Subarray
# eg: [-2, -3, 4, -1, -2, 1, 5, -3] --> 7
# eg: [1,2,-1,3,10,10,-10,-1] --> 29
# eg: [-5,-10,-3] --> -3

def max_cont_sub_arr(arr):
    if len(arr) == 0:
        return None
    cur_sum = max_sum = arr[0]
    for num in arr[1:]:
        cur_sum = max(cur_sum + num, num)
        max_sum = max(cur_sum, max_sum)
    return max_sum

print(max_cont_sub_arr([-2,-3,4,-1,-2,1,5,-3]))