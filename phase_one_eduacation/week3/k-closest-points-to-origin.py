class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda p: sqrt(p[0]*p[0] + p[1]*p[1]))

        return points[:k]