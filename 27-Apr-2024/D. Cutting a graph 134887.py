# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

import sys
input = lambda: sys.stdin.readline().strip()

n, m, k = map(int, input().split())

p = [i for i in range(n)]
size = [0] * n

def get(x):
    a = x
    while a != p[a]:
        a = p[a]
    
    while x != p[x]:
        temp = p[x]
        p[x] = a
        x = temp

    return x

def union(x, y):
    px, py = get(x), get(y)

    if px != py:
        if size[px] > size[py]:
            px, py = py, px
        
        p[px] = py
        size[py] += size[px]


ops = []
for _ in range(m):
    input()
for _ in range(k):
    ops.append(input().split())

ans = []

for i in range(len(ops) - 1, -1, -1):
    a,x,y = ops[i]
    x = int(x) - 1
    y = int(y) - 1
    if a == 'ask':
        ans.append(get(x) == get(y))

    else:
        union(x, y)

for i in range(len(ans) - 1, - 1, -1):
    if ans[i]:
        print('YES')
    else:
        print('NO')