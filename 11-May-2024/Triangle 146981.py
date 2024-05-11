# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def foo(i, j):
            if i == len(triangle):
                return 0
            
            return min(foo(i + 1, j), foo(i + 1, j + 1)) + triangle[i][j]
        
        return foo(0, 0)