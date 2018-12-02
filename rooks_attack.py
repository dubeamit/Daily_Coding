# Can Rooks attack one another
# eg: [[1,0,0,0],       1--> Rook
#      [0,1,0,0],       0--> NO Piece
#      [0,0,0,1],       return True if none of rooks attack each one.
#      [0,0,0,0]]       else return False

# BRUTE FORCE APPROACH

def rooks_attack(chessboard):
    for i in range(len(chessboard)):
        for j in range(len(chessboard[i])):
            if i != j and (chessboard[i][i] == chessboard[j][i] == 1 or chessboard[i][i] == chessboard[i][j] == 1):
                return False
    return True

mat = [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,0,0]]
print(rooks_attack(mat))