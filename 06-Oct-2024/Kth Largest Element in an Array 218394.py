# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        
        for _ in range(len(nums) - k):
            heappop(nums)
        
        return heappop(nums)