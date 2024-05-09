# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0

        for i in range(right.bit_length()):
            if  (1 << i) & left and (1 << i) & right and (right ^ (1 << i)) < left:
                res += 1 << i
        
        return res