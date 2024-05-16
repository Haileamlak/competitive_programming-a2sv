# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        
        dp[0] = matrix[0]
        
        for row in range(1, m):
            dp[row][0] = matrix[row][0] + min(dp[row - 1][1], dp[row - 1][0])
            
            for col in range(1, n - 1):
                dp[row][col] = matrix[row][col] + min(dp[row - 1][col - 1], dp[row - 1][col], dp[row - 1][col + 1])

            dp[row][n - 1] = matrix[row][n - 1] + min(dp[row - 1][n - 2], dp[row - 1][n - 1])

        return min(dp[m - 1])