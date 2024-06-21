# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31, -1, -1):
            res |= (1 if ((1 << i) & n) else 0) << (31 - i)
        
        return res