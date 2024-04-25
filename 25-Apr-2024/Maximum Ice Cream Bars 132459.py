# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        high = max(costs)
        count = [0 for _ in range(high)]

        for cost in costs:
            count[cost - 1] += 1
        
        res = 0
        i = 1
        while i <= high  and coins > 0:
            bars = min((coins // i), count[i - 1])
            coins -= bars * (i * 1)
            res += bars

            i += 1
        
        return res
        
        
        