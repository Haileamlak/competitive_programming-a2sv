# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

from math import inf

import sys
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

parent = [i for i in range(n)]
size = [1 for _ in range(n)]

mmin = [i + 1 for i in range(n)]
mmax = [i + 1 for i in range(n)]

def get(x):
    temp = x
    while temp != parent[temp]:
        temp = parent[temp]
    
    while x != parent[x]:
        next_par = parent[x]
        parent[x] = temp
        x = next_par
    
    return x

def union(x, y):
    par1 = get(x)
    par2 = get(y)

    _min = min(mmin[par1], mmin[par2], x + 1, y + 1)
    _max = max(mmax[par1], mmax[par2], x + 1, y + 1)

    if par1 != par2:
        if size[par1] < size[par2]:
            par1, par2 = par2, par1

        parent[par2] = par1
        size[par1] += size[par2]
        mmin[par1] = _min
        mmax[par1] = _max
        

for _ in range(m):
    action = input().split()

    if action[0] == 'union':
        union(int(action[1]) - 1, int(action[2]) - 1)
    else:
        par = get(int(action[1]) - 1)
        print(mmin[par], mmax[par], size[par])