class Solution:
    def getLeftMost(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

    def getRightMost(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = self.getLeftMost(nums, target)
        end = self.getRightMost(nums, target)

        if start <= end:
            return [start, end]
        
        return [-1, -1]
