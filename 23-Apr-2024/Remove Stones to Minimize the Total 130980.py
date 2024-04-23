# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        temp = [-pile for pile in piles]
        heapify(temp)
        
        while k:
            x = -heappop(temp)
            x = ceil(x / 2)
            heappush(temp, -x)

            k -= 1
        
        return -sum(temp)