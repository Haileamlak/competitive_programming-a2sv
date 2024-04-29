# Problem: Monkeys - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/E

n, m = map(int, input().split())
edges = []
for i in range(n):
    a, b = map(int, input().split())
    edges.append((a, b))

removed = []
for i in range(m):
    a, b = map(int, input().split())
    removed.append((a, b))

removed_set = set(removed)

parent = {i: i for i in range(1,n+1)}
time = {i:float('inf') for i in range(1, n +1 )}

def get(x):
    if x == parent[x]:
        return (x, time[x])
    
    par = get(parent[x])
    time[x] = min(time[x], par[1])
    parent[x] = par[0]

    return (parent[x], time[x])

def union(x, y, t):
    px, tx = get(x)
    py, ty = get(y)

    if px != py:
        if px == 1:
            parent[py] = px
            time[py] = min(ty, t)
        else:
            parent[px]  = py
            time[px] = min(tx, t)

for i, (u, v) in enumerate(edges):
    if u != -1 and (i + 1, 1) not in removed_set:
        union(i + 1, u, float('inf'))
    if v != -1 and (i + 1, 2) not in removed_set:
        union(i + 1, v, float('inf'))

removed.reverse()
for i,( u, v) in enumerate(removed):
    union(u, edges[u - 1][v - 1], m - i - 1)

for i in range(1, n + 1):
    if get(i)[1] < float('inf'):
        print(time[i])
    else:
        print(-1)