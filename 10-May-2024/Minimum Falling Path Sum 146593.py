# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        @cache
        def falling(row, col):
            if col < 0 or col >= n:
                return float('inf')

            if row == m:
                return 0

            return min(falling(row + 1, col - 1), falling(row + 1, col), falling(row + 1, col + 1)) + matrix[row][col]

        res = float('inf')
        for col in range(n):
            res = min(res, falling(0, col))
        
        return res