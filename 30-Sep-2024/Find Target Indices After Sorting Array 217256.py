# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        return range(left, right)