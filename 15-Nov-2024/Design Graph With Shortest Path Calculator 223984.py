# Problem: Design Graph With Shortest Path Calculator - https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        for u, v, weight in edges:
            self.graph[u].append((v, weight))

    def addEdge(self, edge: List[int]) -> None:
        u, v, weight = edge
        self.graph[u].append((v, weight))

    def shortestPath(self, node1: int, node2: int) -> int:
        queue = deque([(node1, 0)])
        
        visited = {}
        visited[node1] = 0
        
        res = float('inf')
        while queue:
            curr, cost = queue.popleft()
            if curr == node2:
                res = min(res, cost)
            
            for neighbour, weight in self.graph[curr]:
                if neighbour not in visited or cost + weight < visited[neighbour]:
                    visited[neighbour] = cost + weight
                    queue.append((neighbour, cost + weight))
        
        if res == float('inf'):
            return -1
        
        return res


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)