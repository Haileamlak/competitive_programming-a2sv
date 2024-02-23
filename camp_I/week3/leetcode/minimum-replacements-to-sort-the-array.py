class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        target_max = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            num_of_split = ceil(nums[i] / target_max)
            res += num_of_split - 1
            target_max = nums[i] // num_of_split
        
        return res