# Problem: Magic Squares In Grid - https://leetcode.com/problems/magic-squares-in-grid/

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0

        def is_magic_square(start_row, start_col):
            # main diagonal sum
            _sum = 0
            unique = set()
            for i in range(3):
                if grid[start_row + i][start_col + i] in unique:
                    return False

                _sum += grid[start_row + i][start_col + i]
                unique.add(grid[start_row + i][start_col + i])

            # other diagonal sum
            curr = 0
            unique = set()
            for i in range(3):
                if grid[start_row + 2 - i][start_col + i] in unique:
                    return False

                curr += grid[start_row + 2 - i][start_col + i]
                unique.add(grid[start_row + 2 - i][start_col + i])
            
            if curr != _sum:
                return False

            total = 0
            for i in range(start_row, start_row + 3):
                curr = 0
                unique = set()
                for j in range(start_col, start_col + 3):
                    if grid[i][j] in unique:
                        return False

                    curr += grid[i][j]
                    unique.add(grid[i][j])
                
                if curr != _sum:
                    return False
                
                total += curr
            
            if total != sum(range(1, 10)):
                return False

            for j in range(start_col, start_col + 3):
                curr = 0
                unique = set()
                for i in range(start_row, start_row + 3):
                    if grid[i][j] in unique or not (0 < grid[i][j] < 10):
                        return False

                    curr += grid[i][j]
                    unique.add(grid[i][j])
                
                if curr != _sum:
                    return False

                total += curr
            
            return True
        
        res = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if is_magic_square(i, j):
                    res += 1
                
        return res