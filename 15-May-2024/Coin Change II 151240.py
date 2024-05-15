# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = [{} for _ in range(len(coins))]

        def _change(i, amount):
            if amount == 0:
                return 1

            if i == len(coins):
                return 0

            if amount in memo[i]:
                return memo[i][amount]
            
            res = 0
            for j in range(amount // coins[i] + 1):
                res += _change(i + 1, amount - coins[i] * j)

            memo[i][amount] = res
            return res

        return _change(0, amount)