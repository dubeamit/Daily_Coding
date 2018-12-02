# Remove all consecutive duplicates from the string
def del_duplicates(st):
    if len(st) == 0:
        return None
    lst = []
    for i in range(1,len(st)):
        if st[i-1] != st[i]:
            lst.append(st[i-1])
    lst.append(st[len(st)-1])
    str1 = ''.join(lst)
    return str1

print(del_duplicates("aaaaabbbbbb"))       
print(del_duplicates("geeksforgeeks"))
print(del_duplicates("aabccba"))