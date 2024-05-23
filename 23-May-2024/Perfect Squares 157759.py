# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        
        @cache
        def _numSquares(n):
            if n < 0:
                return float('inf')
            
            if n == 0:
                return 0

            return min( 
                        1 + _numSquares(n - i * i) 
                        for i in range(1, int(sqrt(n)) + 1)
                    )
        
        return _numSquares(n)