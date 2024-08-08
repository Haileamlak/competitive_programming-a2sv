# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for seek in range(len(nums) - 1):
            if nums[seek] == nums[seek + 1] and nums[seek] != 0:
                nums[seek + 1] = 0
                nums[seek] *= 2

        placeholder = 0
        for seeker in range(len(nums)):
            if nums[seeker] != 0:
                nums[seeker], nums[placeholder] = 0, nums[seeker]
                placeholder += 1

        return nums