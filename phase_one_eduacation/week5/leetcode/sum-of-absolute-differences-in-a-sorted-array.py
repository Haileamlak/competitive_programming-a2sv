class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0 for _ in range(len(nums))]
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]

        suffix = [0 for _ in range(len(nums))]
        suffix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] = nums[i]*(i + 1) - prefix[i] + suffix[i] - nums[i] * (len(nums) - i)
        
        return res