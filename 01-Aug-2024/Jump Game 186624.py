# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        right = n - 1
        for left in range(n - 2, -1, -1):
            if nums[left] >= right - left:
                right = left

        return right == 0