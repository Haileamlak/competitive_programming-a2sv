# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)
        
        for (a, b), value in zip(equations, values):
            adj_list[a].append((b, value))
            adj_list[b].append((a, 1 / value))

        def dfs(numerator, denominator, visited):
            if numerator == denominator:
                return 1

            visited.add(numerator)

            for num, value in adj_list[numerator]:
                if num not in visited:
                    temp = dfs(num, denominator, visited)
                    if temp > -1:
                        return value * temp
            
            return -1

        res = []
        for a, b in queries:
            if a in adj_list and b in adj_list:
                res.append(dfs(a, b, set([a])))
            else:
                res.append(-1)
        
        return res