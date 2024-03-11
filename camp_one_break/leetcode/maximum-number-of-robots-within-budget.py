class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
        def cost(k):
            res = float('inf')
            max_queue = deque()
            for i in range(k - 1):
                while max_queue and chargeTimes[max_queue[-1]] <= chargeTimes[i]:
                    max_queue.pop()
                
                max_queue.append(i)

            curr_sum = sum(runningCosts[:k - 1])
            for i in range(k - 1, len(runningCosts)):

                if max_queue and i - max_queue[0] >= k:
                    max_queue.popleft()
                    
                while max_queue and chargeTimes[max_queue[-1]] <= chargeTimes[i]:
                    max_queue.pop()
                
                max_queue.append(i)

                curr_sum += runningCosts[i]
                res = min(res, chargeTimes[max_queue[0]] + k * curr_sum)
                curr_sum -= runningCosts[i - k + 1]
            
            return res
        
        minimum, maximum = 1, len(runningCosts)
        while minimum <= maximum:
            mid = minimum + (maximum - minimum) // 2
            if cost(mid) <= budget:
                minimum = mid + 1
            else:
                maximum = mid - 1
        
        return maximum