# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        right_sum = sum(nums)
        left_sum = 0
        for i in range(n):
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i
        
            left_sum += nums[i]

        return -1