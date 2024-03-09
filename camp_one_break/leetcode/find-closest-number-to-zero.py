class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        index = bisect_left(nums, 0)

        if index == 0:
            return nums[0]

        if index == len(nums):
            return nums[-1]

        if abs(nums[index - 1]) < abs(nums[index]):
            return nums[index - 1]

        return nums[index]