class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        prefix_sum = [[0 for _ in range(n)] for _ in range(m)]

        for row in range(m):
            prefix_sum[row][0] = grid[row][0]
            for col in range(1, n):
                prefix_sum[row][col] = prefix_sum[row][col - 1] + grid[row][col]
        
        max_hour = 0
        
        row = 2
        col = 2
        while row < m:
            hourglass1 = prefix_sum[row - 2][col]
            hourglass2 = prefix_sum[row][col]
            hourglass = hourglass1 + hourglass2 + grid[row - 1][col - 1]

            max_hour = max(max_hour, hourglass)
            row += 1

        for row in range(2, m):
            for col in range(3, n):
                hourglass1 = prefix_sum[row - 2][col] - prefix_sum[row - 2][col - 3]
                hourglass2 = prefix_sum[row][col] - prefix_sum[row][col - 3]
                hourglass = hourglass1 + hourglass2 + grid[row - 1][col - 1]

                max_hour = max(max_hour, hourglass)

        return max_hour