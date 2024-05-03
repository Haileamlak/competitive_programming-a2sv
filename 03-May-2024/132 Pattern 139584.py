# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False

        minimum = [nums[0] for _ in range(len(nums))]
        for i in range(1, len(nums)):
            minimum[i] = min(minimum[i - 1], nums[i])

        stack = []
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == minimum[i]:
                continue
            
            while stack and stack[-1] <= minimum[i]:
                stack.pop()

            if stack and stack[-1] < nums[i]:
                return True

            stack.append(nums[i])

        return False