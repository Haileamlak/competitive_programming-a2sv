# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = defaultdict(tuple)

        def find(a):
            if a not in parent:
                parent[a] = a

            while a != parent[a]:
                a = parent[a]

            return a

        for x, y in stones:
            row_parent = find(('r', x))
            col_parent = find(('c', y))

            parent[row_parent] = col_parent
        
        res = defaultdict(int)

        for x, y in stones:
            res[find(('r', x))] += 1
        
        answer = 0
        for count in res.values():
            answer += count - 1
        
        return answer