# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

x = int(input())
count = 0
while x:
    x &= x - 1
    count += 1

print(count)