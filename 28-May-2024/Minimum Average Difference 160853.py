# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)

        res = (-1, float('inf'))
        prefix_sum = 0
        suffix_sum = sum(nums)
        for i in range(n - 1):
            prefix_sum += nums[i]
            suffix_sum -= nums[i]
            absolute_difference = abs(prefix_sum // (i + 1) - suffix_sum // (n - i - 1))
            if absolute_difference < res[1]:
                res = (i, absolute_difference)
        
        if (prefix_sum + nums[-1]) // n < res[1]:
            return n - 1
        
        return res[0]