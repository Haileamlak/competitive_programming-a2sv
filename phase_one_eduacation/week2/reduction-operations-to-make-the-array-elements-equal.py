class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        ops = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                ops += i

        return ops