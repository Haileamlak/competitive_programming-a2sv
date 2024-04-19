# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available_tasks = []
        unavailable_tasks = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        heapify(unavailable_tasks)

        res = []
        curr_time = 1
        while available_tasks or unavailable_tasks:
            while unavailable_tasks and unavailable_tasks[0][0] <= curr_time:
                enqueue_time, processing_time, index = heappop(unavailable_tasks)
                heappush(available_tasks, (processing_time, index))
            
            if available_tasks:
                processing_time, index = heappop(available_tasks)
                res.append(index)
                curr_time += processing_time
            else:
                enqueue_time, processing_time, index = heappop(unavailable_tasks)
                res.append(index)
                curr_time += processing_time + (enqueue_time - curr_time)
        
        return res