# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        has_secret = [False for i in range(n)]
        has_secret[0] = True
        has_secret[firstPerson] = True

        def get(x, parent):
            if x not in parent:
                parent[x] = x

            root = x
            while root != parent[root]:
                root = parent[root]
            
            while x != parent[x]:
                x, parent[x] = parent[x], root
            
            return x
        
        def union(x, y, parent, secret):
            px, py = get(x, parent), get(y, parent)

            if px != py:
                parent[px] = py
                if secret[px] or secret[py]:
                    secret[py] = True

        meetings.sort(key = lambda x : x[2])

        i = 0
        while i < len(meetings):
            secret = {}
            parent = {}
            j = k = i
            curr = meetings[i][2]
            while j < len(meetings) and meetings[j][2] == curr:
                x, y = meetings[j][0], meetings[j][1]
                secret[x] = secret[get(x, parent)] if x in secret else has_secret[x]
                secret[y] = secret[get(y, parent)] if y in secret else has_secret[y]

                union(x, y, parent, secret) 
                j += 1

            for t in range(k, j):
                x, y = meetings[t][0], meetings[t][1]
                if secret[get(x, parent)] or secret[get(y, parent)]:
                    has_secret[x] = True
                    has_secret[y] = True
        
            i = j
        
        res = []
        for i in range(n):
            if has_secret[i]:
                res.append(i)

        return res