class Solution:
    def findMin(self, nums: List[int]) -> int:
        def are_all_equal(left, right):
            for i in range(left, right):
                if nums[i] != nums[i + 1]:
                    return False
            
            return True

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            if nums[mid] > nums[(mid + 1) % len(nums)]:
                return nums[(mid + 1) % len(nums)]
            
            if nums[left] == nums[right] == nums[mid] :
                if are_all_equal(left, mid):
                    left = mid + 1
                else:
                    right = mid - 1

            elif nums[right] >= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return nums[left]