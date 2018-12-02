# Counting no. of negative number in a matrix
# number increases as the row and column increase
# eg: [[-4,-3,-1,1],
#      [-2,-2,1, 2],
#      [-1, 1,2, 3],
#      [1, 2, 3, 4]] should return 6

def count_negatives(mat):
    count = 0
    row = 0
    col = len(mat) - 1
    while col >= 0 and row < len(mat):
        if mat[row][col] < 0:
            count += col + 1
            row += 1
        else:
            col -= 1
    return count

mat = [[-4,-3,-1,1],
      [-2,-2,1, 2],
      [-1, 1,2, 3],
      [1, 2, 3, 4]]

print("No. of negative numbers are", count_negatives(mat))