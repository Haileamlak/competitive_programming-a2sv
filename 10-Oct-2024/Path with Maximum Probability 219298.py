# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        visited = set()
        heap = [(-1, start_node)]
        while heap:
            curr_prob, node = heappop(heap)
            curr_prob *= -1

            if node in visited:
                continue
            
            if node == end_node:
                return curr_prob

            visited.add(node)
            for nbr, prob in graph[node]:
                if nbr in visited:
                    continue
                
                heappush(heap, (- (curr_prob * prob), nbr))

        return 0