# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = {i:i for i in range(n)}
        min_distance = [inf for _ in range(n)]

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x
        
        def union(x, y, distance):
            px = find(x)
            py = find(y)

            min_dist = min(min_distance[px], min_distance[py], distance)

            if px != py:
                parent[py] = px
            
            min_distance[px] = min_dist
        
        for x, y, distance in roads:
            union(x - 1, y - 1, distance)

        return min_distance[find(0)]