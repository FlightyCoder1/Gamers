chess_map_from_alpha_to_index = {
   "a" : 0,
   "b" : 1,
   "c" : 2,
   "d" : 3,
   "e" : 4,
   "f" : 5,
   "g" : 6,
   "h" : 7
}
chess_map_from_index_to_alpha = {
   0: "a",
   1: "b",
   2: "c",
   3: "d",
   4: "e",
   5: "f",
   6: "g",
   7: "h"
}
def getKnightMoves(pos, chessBoard):
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_alpha_to_index[column]
    i,j = row, column
    solutionMoves = []
    try:
        temp = chessBoard[i + 1][j - 2]
        solutionMoves.append([i + 1, j - 2])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j - 1]
        solutionMoves.append([i + 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j + 1]
        solutionMoves.append([i + 2, j + 1])
    except:
        pass
    try:
       temp = chessBoard[i + 1][j + 2]
       solutionMoves.append([i + 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j + 2]
        solutionMoves.append([i - 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j + 1]
        solutionMoves.append([i - 2, j + 1])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j - 1]
        solutionMoves.append([i - 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j - 2]
        solutionMoves.append([i - 1, j - 2])
    except:
        pass

    # Filter all negative values
    temp = [i for i in solutionMoves if i[0] >=0 and i[1] >=0]
    allPossibleMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    allPossibleMoves.sort()
    return allPossibleMovesdef getKnightMoves(pos, chessBoard):
    column, row = list(pos.strip().lower())
    row = int(row) - 1
   def getrook
    column = chess_map_from_alpha_to_index[column]
    i,j = row, column
    solutionMoves = []
    try:
        temp = chessBoard[i + 1][j - 2]
        solutionMoves.append([i + 1, j - 2])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j - 1]
        solutionMoves.append([i + 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j + 1]
        solutionMoves.append([i + 2, j + 1])
    except:
        pass
    try:
       temp = chessBoard[i + 1][j + 2]
       solutionMoves.append([i + 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j + 2]
        solutionMoves.append([i - 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j + 1]
        solutionMoves.append([i - 2, j + 1])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j - 1]
        solutionMoves.append([i - 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j - 2]
        solutionMoves.append([i - 1, j - 2])
    except:
        pass

    # Filter all negative values
    temp = [i for i in solutionMoves if i[0] >=0 and i[1] >=0]
    allPossibleMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    allPossibleMoves.sort()
    return allPossibleMoves
 
