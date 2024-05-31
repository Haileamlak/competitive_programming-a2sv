# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = defaultdict(int)
        my_graph = [[] for _ in range(n)]

        for node in range(n):
            for adj_node in graph[node]:
                indegree[node] += 1
                my_graph[adj_node].append(node)

        res = []
        queue = deque([node for node in range(n) if node not in indegree])
        while queue:
            curr_node = queue.popleft()
            res.append(curr_node)

            for adj_node in my_graph[curr_node]:
                indegree[adj_node] -= 1

                if not indegree[adj_node]:
                    queue.append(adj_node)
        
        return sorted(res)