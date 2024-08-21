# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        def xor(x, y):
            return x ^ y

        _max = (1 << maximumBit) - 1

        total_xor = reduce(xor, nums)

        res = []
        for i in range(len(nums)):
            k = (((1 << maximumBit) - 1) ^ total_xor) & _max
            res.append(k)

            total_xor ^= nums[-1 - i]
        
        return res