# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def buy_sell(i, buy):
            if i >= len(prices):
                return 0
            
            buy = min(buy, prices[i])
            res = buy_sell(i + 1, buy)
            
            if prices[i] > buy:
                res = max(res, prices[i] - buy + buy_sell(i + 2, prices[i]))
            
            return res
        
        return buy_sell(0, float('inf'))