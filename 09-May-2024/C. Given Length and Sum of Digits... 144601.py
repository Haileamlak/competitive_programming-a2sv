# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m, s = map(int, input().split())
 
if m == 1 and s == 0:
    print(0, 0)
    exit()

elif not s:
    print(-1, -1)
    exit()
 
max_num = [0]*m
for index in range(m):
    delta = min(9, s)
    max_num[index] += delta
    s -= delta

if s:
    print(-1, -1)
    exit()

min_num = max_num[::-1]
for index in range(m):
    if min_num[index] != 0: 
        min_num[index] -= 1
        min_num[0] += 1
        break

max_str = ''.join(map(str, max_num))
min_str = ''.join(map(str, min_num))
print(min_str, max_str)