# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapify(heap)

        for i in range(len(heights) - 1):
            if heights[i] < heights[i + 1]:
                heappush(heap, heights[i + 1] - heights[i])
                if len(heap) > ladders:
                    curr = heappop(heap)
                    bricks -= curr
                
                if bricks < 0:
                    return i
        
        return len(heights) - 1