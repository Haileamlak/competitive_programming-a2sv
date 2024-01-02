class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        tasks.sort(reverse=True)
        processorTime.sort()
        n = len(processorTime)
        res = 0
        for i in range(n):
            res = max(processorTime[i] + tasks[i*4], res)   

        return res    