class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        def start_of_negative(row, minn):
            low = minn
            high = len(grid[0]) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if grid[row][mid] < 0:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return low
        
        res = 0
        start = 0
        for i in range(len(grid) - 1, -1, -1):
            start = start_of_negative(i, start)
            res += len(grid[0]) - start
    
        return res