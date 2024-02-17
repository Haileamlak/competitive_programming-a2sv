class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        res[0] = nums[0]
        for i in range(1,len(nums)):
            res[i] = res[i - 1] + nums[i]

        return res