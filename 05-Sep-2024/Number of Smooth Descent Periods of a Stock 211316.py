# Problem: Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        count = 1

        for i in range(1, len(prices)):
            if prices[i] != prices[i - 1] - 1:
                res += count * (count + 1) // 2
                count = 0

            count += 1

        res += count * (count + 1) // 2

        return res