# Problem: E - Weighted Cycle Search - https://codeforces.com/gym/520688/problem/E

from collections import defaultdict, deque

for i in range(int(input())):
    n, m = map(int, input().split())
    edges = []
    graph = defaultdict(list)
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    edges.sort(key = lambda x : x[2], reverse=True)

    # # def dfs(curr, color, temp,dad, dd):
    # #     color[curr] = 1
    # #     dad[curr] = dd
    # #     for nbr, w in graph[curr]:
    # #         if color[nbr] == 0:
    # #             temp[nbr] = curr
    # #             x = dfs(nbr, color, temp, dad, dd)
    # #             if x:
    # #                 return x
                
    # #         elif dad[nbr] == dd:
    # #             return curr
            
                
            
    # #     # color[curr] = 1
    # #     return None

    # def bfs(curr,x, temp, seen):
    #     seen.add(curr)
    #     visited = set([curr, x])
    #     queue = deque([curr])

    #     while queue:
    #         curr = queue.popleft()

    #         for nbr, w in graph[curr]:
    #             if nbr not in visited:
    #                 seen.add(nbr)
    #                 visited.add(nbr)
    #                 temp[nbr] = curr
    #                 queue.append(nbr)
    #             elif temp[curr] != nbr:
    #                 return curr
                
    #     return None

    # seen = set()
    # for edge in edges:
    #     if edge[0] not in seen:
    #         temp = {}
    #         temp[edge[1]] = edge[0]
    #         temp[edge[0]] = edge[0]
    #         seen.add(edge[0])
    #         res = bfs(edge[1], edge[0], temp, seen)
        
    #         if res:
    #             start = edge[0]
    #             w = edge[2]
    #             break

    # a = res
    # ans = [a]

    # while a != start:
    #     a = temp[a]
    #     ans.append(a)

    # print(w, len(ans))
    # print(*ans)


    parent = {i:i for i in range(1, n + 1)}

    def get(x):
        root = x
        while root != parent[root]:
            root = parent[root]
        
        while x != parent[x]:
            x, parent[x] = parent[x], root
        
        return x
    
    def union(x, y):
        px, py = get(x), get(y)

        parent[px] = py

    start = end = -1
    
    for u, v, w in edges:
        if get(u) != get(v):
            union(u, v)
        else:
            start = u
            end = v
            aa = w


    # print(parent, start, end)
    
    queue = deque([(start, float('inf'))])
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    
    temp = {}
    while queue:
        curr, w = queue.popleft()

        if curr == end:
            ans = curr
            break
            
        for nbr, ww in graph[curr]:
            if (start, end) == (curr, nbr):
                w = min(w, ww)
            elif not visited[nbr]:
                visited[nbr] = True
                temp[nbr] = curr
                queue.append((nbr, min(w, ww)))
    
    res = []
    x = ans
    while x in temp:
        res.append(x)
        x = temp[x]
    
    res.append(x)
    print(aa, len(res))
    print(*res)