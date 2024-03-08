class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = len(nums) + 1
        
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        mono_queue = deque()

        for i, pi in enumerate(prefix_sum):
            while mono_queue and pi <= prefix_sum[mono_queue[-1]]:
                mono_queue.pop()
                
            while mono_queue and pi - prefix_sum[mono_queue[0]] >= k:
                res = min(res, i - mono_queue.popleft())
            
            mono_queue.append(i)
        
        return res if res != len(nums) + 1 else -1
            