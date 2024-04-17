# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapify(heap)

        i = 0
        while i < len(heights) - 1:
            if heights[i] < heights[i + 1]:
                heappush(heap, heights[i + 1] - heights[i])
                if len(heap) > ladders:
                    curr = heappop(heap)
                    bricks -= curr
                
                if bricks < 0:
                    return i
                    
            i += 1
        
        return i