class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        zero = -1
        start = zero + 1
        deleted = False
        i = 0
        while i < len(nums):
            if nums[i] == 0 and deleted:
                start = zero + 1
                i = start
                deleted = False
                
            elif nums[i] == 0:
                zero = i
                deleted = True
                i += 1

            else:
                i += 1
            
            longest = max(longest, i - start - 1)        

        return longest