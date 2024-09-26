# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> bool:

        seen = set([1])
        heap = [1]
        n -= 1
        while n:
            x = heappop(heap)
            if x * 2 not in seen:
                seen.add(x * 2)
                heappush(heap, x * 2)
                
            if x * 3 not in seen:
                seen.add(x * 3)
                heappush(heap, x * 3)
                
            if x * 5 not in seen:
                seen.add(x * 5)
                heappush(heap, x * 5)
                
            n -= 1

        return heappop(heap)