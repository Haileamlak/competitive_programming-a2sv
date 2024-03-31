class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        ml = mx = -1
        left = -1
        for right in range(len(nums)):
            if nums[right] < minK or nums[right] > maxK:
                left = right
                ml = mx = -1

            if nums[right] == minK:
                ml = right

            if nums[right] == maxK:
                mx = right

            
            if ml != -1 and mx != -1:
                res += min(ml, mx) - left
        
        return res
