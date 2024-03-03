class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[i] if i % 2 == 0 else 0 for i in range(len(nums)))