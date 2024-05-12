# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        directions = [(1, 1), (-1, -1), (-1, 1), (1, -1), (1, 0), (-1, 0), (0, -1), (0, 1)]
        res = []
        for row in range(1, m - 1):
            res.append([])
            for col in range(1, n - 1):
                curr = grid[row][col]
                for i, j in directions:
                    r, c = row + i, col + j
                    curr = max(curr, grid[r][c])

                res[-1].append(curr)
        
        return res