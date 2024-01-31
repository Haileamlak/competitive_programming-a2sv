class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            soduku = set()
            for j in range(9):
                if board[i][j] == '.':
                    pass
                elif board[i][j] in soduku:
                    return False
                else:
                    soduku.add(board[i][j])

        for j in range(9):
            soduku = set()
            for i in range(9):
                if board[i][j] == '.':
                    pass
                elif board[i][j] in soduku:
                    return False
                else:
                    soduku.add(board[i][j])

        for i in range(3, 10, 3):
            for j in range(3, 10, 3):
                soduku = set()
                for k in range(i - 3, i):
                    for l in range(j - 3, j):
                        if board[k][l] == '.':
                            pass
                        elif board[k][l] in soduku:
                            return False
                        else:
                            soduku.add(board[k][l])
                            
        return True