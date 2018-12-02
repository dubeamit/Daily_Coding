#Print anti-diagonal of a N*N square Matrix
# [[1,2,3],[4,5,6],[7,8,9]]---> [[1],[2,4],[3,5,7],[6,8],[9]]

def anti_diagonal(A):
    n = len(A)
    AD = [[] for _ in range(n*2-1)]
    for i in range(n):
        for j in range(n):
            AD[i+j].append(A[i][j])
    return AD

print(anti_diagonal([[1,2,3],[4,5,6],[7,8,9]]))
print(anti_diagonal([[1,2],[3,4]]))