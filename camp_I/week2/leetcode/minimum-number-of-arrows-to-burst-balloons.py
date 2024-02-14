class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        points.sort(key=lambda x:x[0])

        res = 1
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                end = points[i][1]
                res += 1
            else:
                end = min(points[i][1], end)
        
        return res