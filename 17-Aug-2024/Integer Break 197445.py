# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1
            
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        
        return res * n