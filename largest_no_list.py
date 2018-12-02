# Given a list of non negative integers, arrange them such that they form the largest number.
# Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#return str

def largest_no_list(A):
    maxlen = len(str(max(A)))
    if all(v == 0 for v in A):
        return 0
    return ''.join(sorted((str(v) for v in A), reverse= True, key = lambda i: i*(maxlen *2 // len(i))))

print(largest_no_list([1114,472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412 ]))