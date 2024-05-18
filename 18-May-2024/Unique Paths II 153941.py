# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[0] * n for _ in range(m)]

        for row in range(m):
            if grid[row][0]:
                break
            
            dp[row][0] = 1

        for col in range(n):
            if grid[0][col]:
                break
            
            dp[0][col] = 1

        for row in range(1, m):
            for col in range(1, n):
                if grid[row][col] == 0:
                    dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
        
        return dp[m - 1][n - 1]