class Solution:
    def totalNQueens(self, n: int) -> int:
        solutions = 0
        main_diagonals = set()
        other_diagonals = set()
        columns = set()

        def back_track(row):
            nonlocal solutions
            if row == n:
                solutions += 1
                return
            
            for col in range(n):
                if col not in columns and (row + col) not in main_diagonals and (row - col) not in other_diagonals:
                    columns.add(col)
                    main_diagonals.add(row + col)
                    other_diagonals.add(row - col)

                    back_track(row + 1)
                    
                    other_diagonals.remove(row - col)
                    main_diagonals.remove(row + col)
                    columns.remove(col)
        
        back_track(0)
        return solutions