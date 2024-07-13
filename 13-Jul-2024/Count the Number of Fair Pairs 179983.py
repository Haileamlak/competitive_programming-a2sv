# Problem: Count the Number of Fair Pairs - https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        def binary_search_left(i, number):
            left, right = i, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] + number >= lower:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left
        
        def binary_search_right(i, number):
            left, right = i, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] + number <= upper:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return right
        
        nums.sort()
        res = 0
        for i in range(len(nums)):
            right = binary_search_right(i + 1, nums[i])
            left = binary_search_left(i + 1, nums[i])
            res += max(0, right - left + 1)
        
        return res