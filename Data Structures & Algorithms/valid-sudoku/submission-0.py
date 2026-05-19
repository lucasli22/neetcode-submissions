class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowSeen = set()
            colSeen = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in colSeen:
                        return False
                    colSeen.add(board[i][j])
                
                if board[j][i] != ".":
                    if board[j][i] in rowSeen:
                        return False
                    rowSeen.add(board[j][i])
        for i in range(3):
            for j in range(3):
                seen = set()
                for x in range(3 * i, 3 * (i + 1)):
                    for y in range(3 * j, 3 * (j + 1)):
                        if board[x][y] == ".":
                            continue
                        if board[x][y] in seen:
                            return False
                        seen.add(board[x][y])
        return True 

                        