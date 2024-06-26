# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]

        def get(edge):
            if edge == parent[edge]:
                return edge
            
            parent[edge] = get(parent[edge])
            return parent[edge]

        def union(x, y):
            px, py = get(x), get(y)
            if px != py:
                if size[px] > size[py]:
                    px, py = py, px

                parent[px] = py
                size[py] += size[px]

        for u, v in edges:
            union(u, v)
        
        res = 0
        for edge in range(n):
            if edge == parent[edge]:
                res += (size[edge] * (n - size[edge]))

            # Alternatively
            # res += n - size[get(edge)]
            
        return (res // 2)