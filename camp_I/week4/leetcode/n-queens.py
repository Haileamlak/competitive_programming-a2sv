class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        solution = []
        taken_columns = set()
        main_diagonals = set()
        other_diagonals = set()
        def back_track(index):
            if index == n:
                solutions.append(solution.copy())
                return

            row = ['.' for _ in range(n)]
            for i in range(n):
                if i not in taken_columns and (index + i) not in main_diagonals and (index - i) not in other_diagonals:
                    row[i] = 'Q'
                    taken_columns.add(i)
                    main_diagonals.add(index + i)
                    other_diagonals.add(index - i)
                    solution.append(''.join(row))
                    back_track(index + 1)
                    solution.pop()
                    main_diagonals.remove(index + i)
                    other_diagonals.remove(index - i)
                    taken_columns.remove(i)
                    row[i] = '.'
        
        back_track(0)
        return solutions