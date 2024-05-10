# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def back_track(i, _sum):
            if i == len(nums) and _sum == target:
                return 1
            
            if i == len(nums):
                return 0

            return back_track(i + 1, _sum - nums[i]) + back_track(i + 1, _sum + nums[i])

        return back_track(0, 0)