# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        job = [(d, p) for d, p in zip(difficulty, profit)]
        job.sort()

        res = 0
        heap = []
        j = 0
        for i in range(len(worker)):
            while j < len(job) and job[j][0] <= worker[i]:
                heappush(heap, -job[j][1])
                j += 1
            
            if heap:
                curr = -heappop(heap)
                res += curr
                heappush(heap, -curr)
        
        return res