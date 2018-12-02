# Given an m x n matrix of 0s and 1s, if an element is 0, 
# set its entire row and column to 0.
# Do it in place.
import numpy as np
def set_matrix_zero(A):
    n = len(A)      #len of rows
    m = len(A[0])   #len of col
    row_list = []
    col_list = []
    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
                if i not in row_list:
                    row_list.append(i)
                if j not in col_list:
                    col_list.append(j)
    zero_row = [0] * m
    for i in range(n):
        if i in row_list:
            A[i] = zero_row
        for j in range(m):
            if j in col_list:
                A[i][j] = 0
    return np.matrix(A)

print(set_matrix_zero([[0,1,1],[1,1,1],[1,1,1]]))
print()
print(set_matrix_zero([[0,0],[1,0]]))