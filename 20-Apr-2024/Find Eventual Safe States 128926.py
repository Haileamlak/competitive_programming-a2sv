# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = defaultdict(int)

        for node in range(n):
            for adj_node in graph[node]:
                indegree[adj_node] += 1


        color = [0 for _ in range(n)]        

        def dfs(node):
            if color[node] == 2:
                return True
            
            if color[node] == 1:
                return False

            color[node] = 1

            for adj_node in graph[node]:
                if not dfs(adj_node):
                    return False

            color[node] = 2
            return True
        
        res = []
        for node in range(n):
            if dfs(node):
                res.append(node)

        return res