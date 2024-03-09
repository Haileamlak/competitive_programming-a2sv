class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = [-1] * len(intervals)
        index_map = {intervals[i][0]:i for i in range(len(intervals))}
        
        start_index = [interval[0] for interval in intervals]
        start_index.sort()
        
        for i in range(len(res)):
            left, right = 0, len(intervals) - 1

            end = intervals[i][1]
            index = bisect_left(start_index, end)
            
            if index < len(intervals):
                res[i] = index_map[start_index[index]]
        
        return res