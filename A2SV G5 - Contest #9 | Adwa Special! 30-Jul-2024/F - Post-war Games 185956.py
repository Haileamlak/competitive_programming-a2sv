# Problem: F - Post-war Games - https://codeforces.com/gym/513152/problem/F

for i  in range(int(input())):
    n, k = map(int, input().split())
    if k == n:
        print(0)
    else:
        x = (n - (k + 1)) * 3 + 1 + ((k - 1) // 2) * 3 + ((k - 1) % 2) * 1
        print(x)
    