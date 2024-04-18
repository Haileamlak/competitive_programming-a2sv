# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        if len(self.left_heap) == 0 or num < -self.left_heap[0]:
            heappush(self.left_heap, -num)
        else:
            heappush(self.right_heap, num)

        if len(self.left_heap) - len(self.right_heap) == 2:
            heappush(self.right_heap, -heappop(self.left_heap))

        elif len(self.right_heap) - len(self.left_heap) == 2:
            heappush(self.left_heap, -heappop(self.right_heap))

    def findMedian(self) -> float:
        if len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]

        elif len(self.right_heap) > len(self.left_heap):
            return self.right_heap[0]
        
        return (-self.left_heap[0] + self.right_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()