class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        longest = 0
        length = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                length += 1
            
            currWindow = right - left + 1
            if currWindow - length > k:
                if nums[left] == 1:
                    length -= 1
                left += 1
            else:
                longest = max(longest, currWindow)
            
        return longest