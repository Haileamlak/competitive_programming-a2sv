# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i in range(len(timePoints)):
            hour, minute = timePoints[i].split(':')
            timePoints[i] = int(hour) * 60 + int(minute)
        
        timePoints.sort()
        total_minutes_of_a_day = 24 * 60
        res = float('inf')

        for i in range(len(timePoints)):
            difference = abs(timePoints[i] - timePoints[i - 1])
            res = min(res, difference, total_minutes_of_a_day - difference)

        return res