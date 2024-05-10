# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def _change(curr_amount):
            if curr_amount == 0:
                return 0
            
            res = float('inf')
            for c in coins:
                if c <= curr_amount:
                    res = min(res, 1 + _change(curr_amount - c))
            
            return res

        ans = _change(amount)
        return ans if ans < float('inf') else -1