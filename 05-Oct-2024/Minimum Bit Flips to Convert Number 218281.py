# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start ^ goal
    
        count = 0
        while res:
            res &= res - 1 # remove one set bit
            count += 1
        
        return count