class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])  
        res = 0
        l = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[l][1]:
                res += 1
            else:
                l = i
        return res