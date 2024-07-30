# Problem: A - Ascend - https://codeforces.com/gym/526229/problem/A

n = int(input())
a = list(map(int, input().split()))
res = 1
count = 1
for i in range(1, n):
    if a[i] > a[i - 1]:
        count += 1
    else:
        count = 1
    res = max(res, count)

print(res)