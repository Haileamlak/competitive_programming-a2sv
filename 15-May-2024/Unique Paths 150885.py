# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def _uniquePaths(row, col):
            if row >= m or col < 0 or col >= n:
                return 0
            
            if (row, col) == (m - 1, n - 1):
                return 1
            
            return _uniquePaths(row + 1, col) + _uniquePaths(row, col + 1)
        
        return _uniquePaths(0, 0)