# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(sqrt(c))
        while a <= b:
            if a * a + b * b == c:
                return True

            if a * a + b * b < c:
                a += 1
            else:
                b -= 1
        
        return False