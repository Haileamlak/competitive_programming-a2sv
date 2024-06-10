# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        @cache
        def buy_ticket(i):
            if i >= len(days):
                return 0

            return min(
                cost + buy_ticket(bisect_left(days, days[i] + _pass))
                for _pass, cost in zip([1, 7, 30], costs)
            )

        return buy_ticket(0)