# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        queue = deque([nums[0], nums[1], nums[0] + nums[2]])

        for i in range(3, len(nums)):
            queue.append(nums[i] + max(queue[-2], queue[-3]))
            queue.popleft()
        
        return max(queue[-1], queue[-2])