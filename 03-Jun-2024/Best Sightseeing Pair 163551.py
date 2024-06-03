# Problem: Best Sightseeing Pair - https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        curr = values[0]
        res = 0
        for j in range(1, len(values)):
            res = max(res, curr + values[j] - j)
            curr = max(curr, values[j] + j)
        
        return res