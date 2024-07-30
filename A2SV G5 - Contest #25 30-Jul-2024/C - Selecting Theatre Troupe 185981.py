# Problem: C - Selecting Theatre Troupe - https://codeforces.com/gym/535749/problem/C

import sys

from math import comb

n, m, t = map(int, sys.stdin.readline().strip().split())

ans = 0
for b in range(4, t):
    ans += comb(n, b)  * comb(m, t  - b)

print(ans)