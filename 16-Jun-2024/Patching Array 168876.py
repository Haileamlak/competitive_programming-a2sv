# Problem: Patching Array - https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr = res = i = 0
        while i < len(nums) and curr < n:
            if curr - nums[i] < -1:
                res += 1
                curr += curr + 1
            else:
                curr += nums[i]
                i += 1
        
        while curr < n:
            res += 1
            curr += curr + 1
            
        return res