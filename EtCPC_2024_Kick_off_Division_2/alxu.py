a, b = map(int, input().split())
x = 1000000007
res = (a % x + b % x) % x
print(res)