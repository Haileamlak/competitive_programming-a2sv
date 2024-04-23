# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {node: node for node in range(1, n + 1)}
        size = [0 for _ in range(n)]

        def find_parent(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            
            return node
        
        def union(node1, node2):
            parent1 = find_parent(node1)
            parent2 = find_parent(node2)

            if size[parent1 - 1] > size[parent2 - 1]:
                parent[parent2] = parent1
                size[parent1 - 1] += size[parent2 - 1]
            else:
                parent[parent1] = parent2
                size[parent2 - 1] += size[parent1 - 1]
        
        for a, b in edges:
            if find_parent(a) == find_parent(b):
                return [a, b]
            else:
                union(a, b)