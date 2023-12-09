class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        length = 0
        for i in range(len(nums)):
            if nums[i]:
                length += 1
                res = max(length, res)
            else:
                length = 0

        return res 