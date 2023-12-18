class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        row_diff = [0 for _ in range(m)]
        col_diff = [0 for _ in range(n)]
        
        for i in range(m):
            ones = sum(grid[i])
            row_diff[i] = 2 * ones - n
            
        for j in range(n):
            for i in range(m):
                col_diff[j] += grid[i][j]
        
        for i in range(n):
            col_diff[i] = 2 * col_diff[i] - m

        diff = [[row + col for col in col_diff] for row in row_diff]
        
        return diff