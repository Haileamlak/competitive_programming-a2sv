# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        @lru_cache(None)
        def _triangulation(left, right):
            if right - left < 2:
                return 0
            
            res = inf
            curr = values[left] * values[right]
            for i in range(left + 1, right):
                res = min(res, _triangulation(left, i) + _triangulation(i , right) + (values[i] * curr))

            return res
        
        return _triangulation(0, len(values) - 1)