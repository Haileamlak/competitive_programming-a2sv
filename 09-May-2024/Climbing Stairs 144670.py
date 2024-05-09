# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def climb(n):
            if n == 1 or n == 2:
                return n
            
            return climb(n - 1) + climb(n - 2)
        
        return climb(n)