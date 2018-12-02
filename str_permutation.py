def toString(lst):
    return ''.join(lst)

def str_permute(lst, left_index, right_index):
    if left_index == right_index:
        print(toString(lst))
    else:
        for i in range(left_index,right_index+1):
            lst[left_index], lst[i] = lst[i], lst[left_index]
            str_permute(lst,left_index+1, right_index)
            lst[left_index], lst[i] = lst[i], lst[left_index]

string = 'abc'
n = len(string)
lst = list(string)
str_permute(lst, 0, n-1)