# Problem: E - Seamless Flow - https://codeforces.com/gym/519135/problem/E

from collections import defaultdict, deque
from turtle import position


for i in range(int(input())):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    edge_count = defaultdict(int)
    undirected = []    
    directed = []

    for i in range(m):
        
        t, a, b = map(int, input().split())
        if t == 1:
            graph[a].append(b)
            edge_count[b] += 1
            directed.append((a, b))
        else:
            # graph[a].append((b, 0))
            # graph[b].append((a, 0))
            # edge_count2[a] += 1
            # edge_count2[b] += 1
            undirected.append((a, b))


    queue = deque()
    for node in range(1, n + 1):
        if node not in edge_count:
            queue.append(node)

    temp = {}
    res = []
    while queue:
        curr = queue.popleft()
        res.append(curr)
        temp[curr] = len(res)
        for nbr in graph[curr]:
            edge_count[nbr] -= 1
            if edge_count[nbr] == 0:
                queue.append(nbr)


    if len(res) == n:
        for a, b in undirected:
            if temp[a] < temp[b]:
                directed.append((a, b))
            else:
                directed.append((b, a))

        print('YES')
        for a, b in directed:
            print(a, b)
    else:
        print('NO')