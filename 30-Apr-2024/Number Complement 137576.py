# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
            
        res = 0
        i = 0
        while num:
            res += ((num & 1) ^ 1) << i
            num >>= 1
            i += 1
        
        return res