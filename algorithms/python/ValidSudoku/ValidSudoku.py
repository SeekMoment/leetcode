class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = []
        for i in range(3):
            for j in range(3):
                l = []
                for a in range(i * 3, (i + 1) * 3):
                    for b in range(j * 3, (j + 1) * 3):
                        l.append(board[a][b])
                squares.append(l)

        cols = []
        for i in range(len(board)):
            l = []
            for j in range(len(board)):
                l.append(board[j][i])
            cols.append(l)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j].isdigit():
                    if board[i].count(board[i][j]) > 1:
                        return False
                if cols[i][j].isdigit():
                    if cols[i].count(cols[i][j]) > 1:
                        return False
                if squares[i][j].isdigit():
                    if squares[i].count(squares[i][j]) > 1:
                        return False
        return True
