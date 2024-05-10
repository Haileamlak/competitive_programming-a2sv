# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        dp = {}        
        def buy_sell(i, buy):
            if i == len(prices):
                return 0
            
            if (i, buy) in dp:
                return dp[(i, buy)]
            
            res = buy_sell(i + 1, min(buy, prices[i]))
            if prices[i] > buy:
                res = max(res, prices[i] - buy - fee + buy_sell(i + 1, prices[i]))

            dp[(i, buy)] = res 
            return res
        
        return buy_sell(0, inf)