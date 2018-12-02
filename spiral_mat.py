# Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.
# Given the following matrix:
# [[ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]]
# return [1, 2, 3, 6, 9, 8, 7, 4, 5]
def spiral_mat(A):
    m = len(A) # No. of Rows
    n = len(A[0]) # No. of Cols
    lst = []
    T,B,L,R = 0, m-1, 0, n-1 # Top, Bottom, left, Right
    direction = 0
    while L<=R and T<=B:
        if direction == 0: # left to right
            for k in range(L,R+1):
                lst.append(A[L][k])
            T += 1
        elif direction == 1: # top to bottom
            for k in range(T,B+1):
                lst.append(A[k][R])
            R -= 1
        elif direction == 2: # Right to left
            for k in range(R,L-1,-1):
                lst.append(A[B][k])
            B -= 1
        elif direction == 3: # Bottom to top
            for k in range(B,T-1,-1):
                lst.append(A[k][L])
            L += 1
        direction = (direction + 1)% 4
    return lst

print(spiral_mat([
  [1]
]))
print(spiral_mat( [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]))