# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        min_queue = deque()
        max_queue = deque()

        res = 0

        left = 0
        for right in range(n):
            while min_queue and nums[right] <= min_queue[-1][0]:
                min_queue.pop()
            
            min_queue.append((nums[right], right))
            
            while max_queue and nums[right] >= max_queue[-1][0]:
                max_queue.pop()
            
            max_queue.append((nums[right], right))
                
            if min_queue and min_queue[0][1] < left:
                min_queue.popleft()

            if max_queue and max_queue[0][1] < left:
                max_queue.popleft()

            while max_queue[0][0] - min_queue[0][0] > limit:
                if left == min_queue[0][1]:
                    min_queue.popleft()

                if left == max_queue[0][1]:
                    max_queue.popleft()

                left += 1
                
            res = max(res, right - left + 1)

        return res