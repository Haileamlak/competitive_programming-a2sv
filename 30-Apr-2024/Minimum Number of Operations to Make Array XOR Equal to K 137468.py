# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = k
        for num in nums:
            res = res ^ num

        count = 0
        while res:
            res &= res - 1
            count += 1

        return count