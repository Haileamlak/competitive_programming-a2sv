# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [0] * len(grid)
        for row in range(len(grid)):
            row_max[row] = max(grid[row])

        col_max = [0] * len(grid[0])
        for col in range(len(grid[0])):
            max_height = 0
            for row in range(len(grid)):
                max_height = max(max_height, grid[row][col])
            
            col_max[col] = max_height

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                maximum = min(row_max[row], col_max[col])

                if grid[row][col] < maximum:
                    res += maximum - grid[row][col]
            
        return res