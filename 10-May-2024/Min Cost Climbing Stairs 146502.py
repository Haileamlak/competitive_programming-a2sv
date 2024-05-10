# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def climb(i):
            if i >= len(cost):
                return 0
            
            return min(climb(i + 1), climb(i + 2)) + cost[i]
        
        return min(climb(0), climb(1))