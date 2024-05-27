# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False

        group_sum = sum(nums) // k

        dp = {}

        def partition(i, mask, curr_sum):
            if mask == (1 << len(nums)) - 1:
                return True
            
            state = (i, mask, curr_sum)
            if state in dp:
                return dp[state]
            
            res = False
            for j in range(len(nums)):

                if not ((1 << j) & mask):
                    if curr_sum + nums[j] < group_sum:
                        res = res or partition(i, mask | (1 << j), curr_sum + nums[j])
                    elif curr_sum + nums[j] == group_sum:
                        res = res or partition(i + 1, mask | (1 << j), 0)
            
            dp[state] = res
            return res
        
        return partition(0, 0, 0)