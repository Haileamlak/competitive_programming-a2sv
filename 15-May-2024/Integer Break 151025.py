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
        # @cache
        # def _break(n):
        #     if n == 1:
        #         return 1
                
        #     if n == 2 or n == 3:
        #         return n - 1
            
        #     res = n

        #     for i in range(1, n // 2 + 1):
        #         res1 = i * (n - i)
        #         res2 = max(i * _break(n - i), (n - i) * _break(i))
        #         res = max(res, res1, res2)
            
        #     return res

        # return _break(n)