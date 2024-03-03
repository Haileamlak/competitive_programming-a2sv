class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        right = len(prices) - 2
        sell = prices[-1]
        buy = sell
        while right >= 0:
            while right >= 0 and prices[right] >= sell:
                sell = prices[right]
                right -= 1

            buy = sell
            while right >= 0 and prices[right] <= buy:
                buy = prices[right]
                right -= 1

            profit += sell - buy
            if right >= 0:
                sell = prices[right]
                
        return profit