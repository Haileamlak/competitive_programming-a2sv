# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while (
                nums[i] - 1 >= 0
                and nums[i] - 1 < len(nums)
                and nums[i] - 1 != i
                and nums[nums[i] - 1] != nums[i]
            ):
            
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp

        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return i + 1

        return len(nums) + 1
