# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount + 1):
                dp[j] = dp[j] + (dp[j - coins[i]] if j >= coins[i] else 0)

        return dp[amount]