# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]

        # -1 = red, 1 = blue
        for u, v in redEdges:
            adj[u].append((v, -1))

        for u, v in blueEdges:
            adj[u].append((v, 1))

        answer = [float('inf')] * n

        queue = deque([(0, -1, 0), (0, 1, 0)])
        visited = set([(0, -1), (0, 1)])

        while queue:
            curr, color, length = queue.popleft()
            answer[curr] = min(answer[curr], length)

            for u, col in adj[curr]:
                if not (u, col) in visited and color != col:
                    queue.append((u, col, length + 1))
                    visited.add((u, col))
            

        for i in range(n):
            if answer[i] == float('inf'):
                answer[i] = -1

        return answer