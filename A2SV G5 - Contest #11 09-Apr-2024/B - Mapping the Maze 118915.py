# Problem: B - Mapping the Maze - https://codeforces.com/gym/515998/problem/B

from collections import defaultdict


n, m = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


count = defaultdict(int)

for v in graph:
    count[len(graph[v])] += 1

if count[n - 1] == 1 and count[1] == n - 1:
    
    print("star topology")
elif count[2] == n - 2 and count[1] == 2:
    print('bus topology')

elif count[2] == n:
    print("ring topology")
else:
    print('unknown topology')    