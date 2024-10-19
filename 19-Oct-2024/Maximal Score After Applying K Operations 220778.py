# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]

        heapify(heap)
        res = 0
        while k:
            curr = -heappop(heap)
            res += curr
            heappush(heap, -ceil(curr / 3))
            k -= 1
        
        return res