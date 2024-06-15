# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capitals: List[int]) -> int:
        temp = [(c, p) for p, c in zip(profits, capitals)]
        temp.sort()
    
        heap = []

        i = 0
        while k > 0:
            while i < len(temp) and temp[i][0] <= w:
                heappush(heap, -temp[i][1])
                i += 1
            
            if not heap:
                break
            else:
                w += -heappop(heap)

            k -= 1
        
        return w