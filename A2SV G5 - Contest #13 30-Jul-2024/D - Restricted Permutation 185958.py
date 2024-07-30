# Problem: D - Restricted Permutation - https://codeforces.com/gym/519135/problem/D


from collections import defaultdict, deque
from heapq import heapify, heappop, heappush
from re import M

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

indegree = defaultdict(int)

temp = set()

for _ in range(m):
    a, b = map(int, input().split())
    if (a, b) not in temp:
        temp.add((a, b))

        graph[a].append(b)

        indegree[b] += 1

# class MyNum:
#     def __init__(self, val):
#         self.val = val

#     def __lt__(self, other):
#         num1 = self.val
#         num2 = other.val
        
#         if (num1, num2) in temp:
#             return True
        
#         if (num2, num1) in temp:
#             return False
        
#         return num1 < num2


queue = [num for num in range(1, n + 1) if num not in indegree]
heapify(queue)

res = []
while queue:
    curr = heappop(queue)
    res.append(curr)
    
    for b in graph[curr]:
        indegree[b] -= 1
        if indegree[b] == 0:
            heappush(queue, b)

if len(res) == n:
    print(*res)
else:
    print(-1)