class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # diagonal = 
        # hor_ver
        min_time = 0
        for i in range(1, len(points)):
            diagonal = min(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))
            min_time += diagonal
            hor_ver = max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1])) - diagonal
            min_time += hor_ver

        return min_time
