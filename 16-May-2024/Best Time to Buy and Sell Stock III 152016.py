# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def _maxProfit(i, bought, no_of_transactions_made):
            if i == len(prices) or no_of_transactions_made == 2:
                return 0
            
            state = (i, bought, no_of_transactions_made)
            
            if state in memo:
                return memo[state]

            res = 0
            if not bought:
                buy = -prices[i] + _maxProfit(i + 1, True, no_of_transactions_made)
                not_buy = _maxProfit(i + 1, False, no_of_transactions_made)
                res = max(buy, not_buy)
            else:
                sell = prices[i] + _maxProfit(i + 1, False, no_of_transactions_made + 1)
                not_sell = _maxProfit(i + 1, True, no_of_transactions_made)
                res = max(sell, not_sell)
            
            memo[state] = res
            
            return memo[state]
        
        return _maxProfit(0, False, 0)