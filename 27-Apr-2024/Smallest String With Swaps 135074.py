# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [i for i in range(len(s))]
        size = [1 for i in range(len(s))]

        def find(x):
            root = x
            while root != parent[root]:
                root = parent[root]
            
            while x != parent[x]:
                temp = parent[x]
                parent[x] = root
                x = temp
            
            return x
        
        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                if size[px] > size[py]:
                    px, py = py, px

                parent[px] = py
                size[py] += size[px] 
        
        for i, j in pairs:
            union(i, j)
        
        groups = defaultdict(list)
        for i in range(len(s)):
            groups[find(i)].append(i)
        
        pointer = {}
        for i in groups:
            groups[i].sort(key = lambda x : s[x])

            pointer[i] = 0
        
        res = []
        for i in range(len(s)):
            x = find(i)
            index = pointer[x]
            res.append(s[groups[x][index]])
            pointer[x] += 1
        
        return ''.join(res)