# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        res = inf
        graph = defaultdict(list)

        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))

        visited = set([1])
        def dfs(node):
            nonlocal res

            for nbr, d in graph[node]:
                res = min(res, d)

                if nbr not in visited:
                    visited.add(nbr)
                    dfs(nbr)
        
        dfs(1)

        return res