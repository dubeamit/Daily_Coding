# Rotate NxN 2D matrix by 90 degree in clockwise direction
# eg: [1 4]     [2 1]
#     [2 5] ==> [5 4]
def rotate_matrix(A):
    l = len(A)
    i = 0
    j = l - 1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1 
        j -= 1
    for i in range(l):
        for j in range(i+1, l):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    return A

print(rotate_matrix([[1, 2, 3],[4,5,6],[7,8,9]]))
print(rotate_matrix([[1,0],[0,1]]))