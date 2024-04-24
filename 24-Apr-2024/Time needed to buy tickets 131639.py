# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        
        for i in range(k + 1):
            res += min(tickets[i], tickets[k])
        
        for i in range(k + 1, len(tickets)):
            res += min(tickets[i], tickets[k] - 1)

        return res