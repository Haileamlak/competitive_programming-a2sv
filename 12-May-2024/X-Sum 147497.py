# Problem: X-Sum - https://codeforces.com/contest/1676/problem/D

from collections import defaultdict

for i in range(int(input())):
    n, m = map(int, input().split())
    chess = []
    for i in range(n):
        row = list(map(int, input().split()))
        chess.append(row)

    count1 = defaultdict(int)
    count2 = defaultdict(int)

    for row in range(n):
        for col in range(m):
            count1[row - col] += chess[row][col]
            count2[row + col] += chess[row][col]
    
    res = 0
    for row in range(n):
        for col in range(m):
            res = max(res, count1[row - col] + count2[row + col] - chess[row][col])
    
    print(res)