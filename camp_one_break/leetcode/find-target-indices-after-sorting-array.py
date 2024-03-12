class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return range(bisect_left(nums, target), bisect_right(nums, target))