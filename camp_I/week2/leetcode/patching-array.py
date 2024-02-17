class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr = 0
        res = 0
        i = 0
        while i < len(nums) and curr < n:
            if curr - nums[i] < -1:
                res += 1
                curr += curr + 1
            else:
                curr += nums[i]
                i += 1
        
        # curr += nums[-1]
        while curr < n:
            res += 1
            curr += curr + 1
            
        return res