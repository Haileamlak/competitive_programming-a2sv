class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # choc1 = 100
        # choc2 = 100

        # for price in prices:
        #     if price < choc2:
        #         choc2 = choc1
        #         choc1 = price

        #     elif price < choc1:
        #         choc1 = price

        # cost = money - choc1 - choc2

        # if cost >= 0:
        #     return cost
        
        prices.sort()
        cost = money - prices[0] - prices[1]
        if cost >= 0:
            return cost
            
        return money