class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = 0
        currMaxTillNow = -inf
        for num in nums:
            currMax = max(num, num + currMax)
            currMaxTillNow = max(currMax, currMaxTillNow)
        
        return currMaxTillNow