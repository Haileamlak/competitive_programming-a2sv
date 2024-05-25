# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums)  - x
        if target < 0:
            return -1
            
        res = -1
        left = 0
        window = 0
        for right in range(len(nums)):
            window += nums[right]
            while window > target:
                window -= nums[left]
                left += 1

            if window == target:
                res = max(res, right - left + 1)
            
        if res == -1:
            return -1
        
        return len(nums) - res