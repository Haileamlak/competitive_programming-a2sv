# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if int(sqrt(c)) - sqrt(c) == 0:
            return True

        for i in range(int(ceil(sqrt(c)))):
            if int(sqrt(c - (i * i))) - sqrt(c - (i * i)) == 0:
                return True
            
        return False