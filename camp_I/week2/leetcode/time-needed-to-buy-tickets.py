class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        # while tickets[k] > 0:
        #     for i in range(len(tickets)):
        #         if tickets[i]:
        #             res += 1
        #             tickets[i] -= 1
                
        #         if tickets[k] == 0:
        #             break
        
        for i in range(k + 1):
            res += min(tickets[i], tickets[k])
        
        for i in range(k + 1, len(tickets)):
            res += min(tickets[i], tickets[k] - 1)

        return res