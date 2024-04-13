# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        
        for right, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                curr_height = height[stack.pop()]
                if stack:
                    left = stack[-1]
                    min_bound_height = min(height[left], h)
                    result += (right - left - 1) * (min_bound_height - curr_height)
            
            stack.append(right)

        return result