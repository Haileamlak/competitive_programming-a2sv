# Problem: C - Maximizing Edges in a Tree - https://codeforces.com/gym/515998/problem/C

from collections import defaultdict


n = int(input())
m = n - 1

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

zero = 0
one = 0
def dfs(node):
    stack = [node]
    color = defaultdict(int)
    color[node] = 1

    zero = 0
    one = 1
    while stack:
        curr = stack.pop()
        
        for v in graph[curr]:
            if not color[v]:
                color[v] = 0 - color[curr]
                stack.append(v)
                
                if color[v] == -1:
                    zero += 1
                else:
                    one += 1
    
    return (zero, one)

temp = dfs(0)

print(temp[0] * temp[1] - m )