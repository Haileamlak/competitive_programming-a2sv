# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def inbound(row, col):
            return (0 <= row < m) and (0 <= col < n)

        def dfs(row, col):
            res = 1
            grid[row][col] = 0

            for i, j in directions:
                new_row, new_col = row + i, col + j
                if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                    res += dfs(new_row, new_col)
            
            return res
            

        res = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        
        return res