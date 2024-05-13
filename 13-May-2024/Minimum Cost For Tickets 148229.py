# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @cache
        def buy_ticket(i):
            if i >= len(days):
                return 0
            
            res = float('inf')
            j = i
            for _pass, cost in zip([1, 7, 30], costs):
                limit = days[i] + _pass
                while j < len(days) and days[j] < limit:
                    j += 1
                
                res = min(res, cost + buy_ticket(j))
            
            return res
        
        return buy_ticket(0)