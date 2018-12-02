def pascal_triangle(N):
    if N < 1:
        return []
    lst = [1]
    lst2 = []
    lst2.append(lst)
    for _ in range(N-1):
        newlist = []
        newlist.append(lst[0])
        for j in range(len(lst)-1):
            newlist.append(lst[j]+lst[j+1])
        newlist.append(lst[-1])
        lst = newlist
        lst2.append(lst)
    return lst2

print(pascal_triangle(5))
print(pascal_triangle(0))
print(pascal_triangle(4))