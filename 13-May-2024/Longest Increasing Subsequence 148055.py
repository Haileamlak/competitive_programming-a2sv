# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        memo = [0] * n
        def dp(i):
            if i == n:
                return 0
            
            if not memo[i]:
                res = 0
                for j in range(i + 1, n):
                    if nums[j] > nums[i]:
                        res = max(res, dp(j))
                
                memo[i] = res + 1
            
            return memo[i]
        
        return max(dp(i) for i in range(n))