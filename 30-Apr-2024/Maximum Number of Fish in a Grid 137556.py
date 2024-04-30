# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        parent = {}
        fishes = defaultdict(int)

        def get(x):
            if x not in parent:
                parent[x] = x
                fishes[x] = grid[x[0]][x[1]]
            
            root = x
            while root != parent[root]:
                root = parent[root]

            while x != parent[x]:
                x, parent[x] = parent[x], root
            
            return x

        def union(x, y):
            px, py = get(x), get(y)

            if px != py:
                parent[px] = py
                fishes[py] += fishes[px]

        def inbound(row, col):
            return (0 <= row < m) and (0 <= col < n)
        
        directions = [(0, 1), (1, 0)]
        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    get((row, col))
                    for i, j in directions:
                        r, c = row + i, col + j
                        if inbound(r, c) and grid[r][c]:
                            union((r, c), (row, col))
        
        res = 0
        for p in parent:
            if p == parent[p]:
                res = max(res, fishes[p])
        
        return res
