# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [-stone for stone in stones]
        heapify(stones_heap)

        while len(stones_heap) > 1:
            y, x = heappop(stones_heap), heappop(stones_heap)
            if y != x:
                heappush(stones_heap, y - x)
        
        return -sum(stones_heap)