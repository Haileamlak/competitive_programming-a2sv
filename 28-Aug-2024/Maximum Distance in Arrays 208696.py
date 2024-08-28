# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)

        max1 = [arrays[0][-1]]
        for i in range(1, m):
            max1.append(max(max1[-1], arrays[i][-1]))
            
        max2 = [0] * m
        max2[-1] = arrays[-1][-1]
        for i in range(m - 2, -1, -1):
            max2[i] = (max(max2[i + 1], arrays[i][-1]))

        res = 0
        res = max(res, max2[1] - arrays[0][0])
        res = max(res, max1[-2] - arrays[-1][0])
        for i in range(1, m - 1):
            res = max(res, max(max1[i - 1], max2[i + 1]) - arrays[i][0])
        
        return res