class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = bisect_left(nums, target)
        end = bisect_right(nums, target)

        if start < end:
            return [start, end - 1]
        
        return [-1, -1]