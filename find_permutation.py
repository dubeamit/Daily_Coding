# Given a positive integer n and a string s consisting only of 
# letters D or I, you have to find any permutation of first 
# n positive integer that satisfy the given input string.
# D means the next number is smaller, 
# while I means the next number is greater.

def find_permutation(n,S):
    lst = [None] * n
    I,D = 1, n
    for i in range(n-1):
        if S[i] == 'I':
            lst[i] = I
            I += 1
        elif S[i] == 'D':
            lst[i] = D
            D -= 1
    if S[n-2] == 'I':
        lst[n-1] = I
    else:
        lst[n-1] = D
    return lst

print(find_permutation(3,'ID'))
print()
print(find_permutation(10,'IDIDDDIDD'))