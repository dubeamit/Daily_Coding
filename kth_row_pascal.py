def kth_row_pascal(A):
    lst = [1]
    for _ in range(A):
        newlist = []
        newlist.append(lst[0])
        for i in range(1,len(lst)):
            newlist.append(lst[i-1]+lst[i])
        newlist.append(lst[-1])
        lst = newlist
    return lst

print(kth_row_pascal(3)) # 0==> [1] so 3 ==>[1,3,3,1]