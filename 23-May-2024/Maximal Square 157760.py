# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        res = 0
        for i in range(m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                res = 1
        
        for j in range(n):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                res = 1
        
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == '1':
                    dp[row][col] = 1 + min(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1])
                    res = max(res, dp[row][col])
        
        return (res * res)