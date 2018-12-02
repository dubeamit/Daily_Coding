global N
N = 4
def isSafe(board, row, col):
    for i in range(col):# check this row on left side
        if board[row][i] == 1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):#check upper diagonal on left side
        if board[i][j] == 1:
            return False
    for i,j in zip(range(row,N,1),range(col,-1,-1)):#Check lower dia on left side
        if board[i][j] == 1:
            return False
    return True
def solveNQUtil(board,col):
    if col >= N: # if all queens are place return true
        return True
    for i in range(N):
        if isSafe(board,i,col):
            board[i][col] = 1
            if solveNQUtil(board,col+1) == True: # recursive call
                return True
            board[i][col] = 0 # no correct postion found
    return False
def solveNQ():
    board = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]] 
    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False 
    printSolution(board)
    return True
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ")
        print()
solveNQ()