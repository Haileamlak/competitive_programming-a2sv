# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = [[] for _ in range(n)]

        for u, v in enumerate(manager):
            if u != headID:
                tree[v].append(u)
        
        def dfs(node):
            if not tree[node]:
                return 0
                
            return informTime[node] + max(dfs(neighbour) for neighbour in tree[node])
        
        return dfs(headID)