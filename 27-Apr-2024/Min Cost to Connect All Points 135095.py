# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        for i in range(len(points)):
            points[i] = tuple(points[i])

        parent = {point: point for point in points}
        size = {point: 1 for point in points}

        def find(x):
            root = x
            while root != parent[root]:
                root = parent[root]
            
            while x != parent[x]:
                x, parent[x] = parent[x], root
            
            return x
        
        def union(x, y):
            px = find(x)
            py = find(y)

            if size[px] > size[py]:
                px, py = py, px
            
            parent[px] = py
            size[py] += size[px]
        

        edges = []
        for i in range(len(points)):
            for j in range(i + 1):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((distance, points[i], points[j]))
        
        heapify(edges)

        cost = 0
        i = 0
        while i < len(points) - 1:
            distance, x, y = heappop(edges)
            if find(x) != find(y):
                union(x, y)
                cost += distance

                i += 1
        
        return cost