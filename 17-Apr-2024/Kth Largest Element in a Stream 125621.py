# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        
        heapify(self.heap)
        
        for _ in range(len(nums) - k):
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)

        if len(self.heap) > self.k:
            heappop(self.heap)

        res = heappop(self.heap)
        heappush(self.heap, res)

        return res

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)