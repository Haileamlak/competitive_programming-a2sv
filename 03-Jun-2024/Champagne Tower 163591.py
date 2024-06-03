# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        dp = [[poured]]
        for row in range(query_row):
            dp.append([0] * (row + 2))
            for col in range(row + 1):
                curr = max(0, (dp[row][col] - 1) / 2)
                dp[row + 1][col] += curr
                dp[row + 1][col + 1] += curr
                
        
        return min(1, dp[query_row][query_glass])