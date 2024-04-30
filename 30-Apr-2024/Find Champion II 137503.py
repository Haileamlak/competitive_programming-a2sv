# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0
            
        indegree = set()
        for a, b in edges:
            indegree.add(b)
        
        def foo(x, y):
            return x ^ y

        if len(indegree) == n - 1:
            return reduce(foo, list(range(n))) ^ reduce(foo, list(indegree))
        
        return -1