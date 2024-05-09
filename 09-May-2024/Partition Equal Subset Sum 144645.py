# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2:
            return False

        memo = {}

        def back_track(i, _sum):
            if i == len(nums):
                return _sum == total_sum / 2
            
            if _sum > total_sum / 2:
                return False
                
            state = (i, _sum)
            if state not in memo:
                memo[state] = back_track(i + 1, _sum + nums[i]) or back_track(i + 1, _sum)
            
            return memo[state]

        return back_track(0, 0)
