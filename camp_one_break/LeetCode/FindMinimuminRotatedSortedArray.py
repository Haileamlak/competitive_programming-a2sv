class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[(mid + 1) % len(nums)]:
                return nums[(mid + 1) % len(nums)]
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        return nums[left]