class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window = 0
        res = len(nums) + 1
        for right in range(len(nums)):
            window += nums[right]
            while window >= target:
                res = min(res, right - left + 1)
                window -= nums[left]
                left += 1
           
        if res > len(nums):
            return 0
        return res