# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for money in range(amount + 1):
                if money - coin >= 0:
                    dp[money] = min(dp[money], dp[money - coin] + 1)
        
        return dp[money] if dp[money] != float('inf') else -1