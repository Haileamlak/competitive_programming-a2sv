# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        res = 0
        left, right = 0, len(nums) - 1
        while(left < right):
            _sum = nums[left] + nums[right]
            if _sum == k:
                res += 1

            if _sum <= k:
                left += 1

            if _sum >= k:
                right -= 1
        
        return res