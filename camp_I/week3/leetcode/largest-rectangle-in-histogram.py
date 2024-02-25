class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                h, index = stack.pop()
                
                max_area = max(max_area, h * (i - index))
                start = index

            stack.append((heights[i], start))
                
        while stack:
            h, index = stack.pop()
            max_area = max(max_area, h * (len(heights) - index))
        
        return max_area
            
