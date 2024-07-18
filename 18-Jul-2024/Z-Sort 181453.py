# Problem: Z-Sort - https://codeforces.com/problemset/problem/652/B

n = int(input())
a = list(map(int, input().split()))

a.sort()
for i in range(n // 2):
    print(a[i], a[n - i - 1], end=' ')

if n % 2:
    print(a[n // 2])