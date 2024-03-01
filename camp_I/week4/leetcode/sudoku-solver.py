class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited_box = [ [set(), set(), set()], 
                        [set(), set(), set()],
                        [set(), set(), set()] ]

        visited_row = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        visited_column = [set(), set(), set(), set(), set(), set(), set(), set(), set()]

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                         
                    visited_row[row].add(board[row][col])
                    visited_column[col].add(board[row][col])
                    visited_box[row // 3][col // 3].add(board[row][col])

        def back_track(row, col):
            if row == 9:
                return True
            
            if board[row][col] != '.': 
                if col == 8:
                    row += 1
                    col = -1

                if back_track(row, col + 1):
                    return True
                
                return False

            for number in range(1, 10):
                x = str(number)
                if (x not in visited_row[row]) and (x not in visited_column[col]) and (x not in visited_box[row // 3][col // 3]):
                    visited_row[row].add(x)
                    visited_column[col].add(x)
                    visited_box[row // 3][col // 3].add(x)
                    board[row][col] = x

                    new_row = row
                    new_col = col

                    if col == 8:
                        new_row += 1
                        new_col = -1

                    if back_track(new_row, new_col + 1):
                        return True

                    board[row][col] = '.'
                    visited_row[row].remove(x)
                    visited_box[row // 3][col // 3].remove(x)
                    visited_column[col].remove(x)

            return False

        back_track(0, 0)