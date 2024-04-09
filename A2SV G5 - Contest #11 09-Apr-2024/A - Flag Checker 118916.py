# Problem: A - Flag Checker - https://codeforces.com/gym/515998/problem/A

from typing import Counter


n, m = map(int, input().split())
res = []
for i in range(n):
    row = (input())
    res.append((Counter(row), row[0]))

if len(res[0][0]) != 1:
    print('NO')
    
else:
    for i in range(1,n):

        if len((res[i][0])) > 1:
            print('NO')
            break
            
        if res[i][1] == res[i - 1][1]:
            print("NO")
            break
    else:
        print('YES')
    