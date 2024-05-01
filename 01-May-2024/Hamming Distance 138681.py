# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        count = 0
        while res:
            res &= (res - 1)
            count += 1
        
        return count