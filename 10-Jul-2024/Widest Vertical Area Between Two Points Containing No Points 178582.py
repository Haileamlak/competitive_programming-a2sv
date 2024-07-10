# Problem: Widest Vertical Area Between Two Points Containing No Points - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        max_area = 0
        points.sort(key=lambda point: point[0])

        for i in range(1, len(points)):
            max_area = max(max_area, points[i][0] - points[i - 1][0])

        return max_area