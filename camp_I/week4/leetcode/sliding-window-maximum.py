class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        result = []
        for i, num in enumerate(nums):
            # remove indexes that are out of the window
            if window and window[0] < i - k + 1:
                window.popleft()
            
            # remove indexes of elements that are smaller than the current number
            while window and nums[window[-1]] < num:
                window.pop()
            
            window.append(i)

            # check if we have a window of length k
            if i >= k -1:
                result.append(nums[window[0]])
        
        return result