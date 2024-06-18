# Problem: Minimal string - https://codeforces.com/contest/797/problem/C

w = input()

a = [w[-1]] * len(w)

for i in range(len(w) - 2, -1, -1):
    a[i] = min(w[i], a[i + 1])

res = []
s = []

for i in range(len(w)):
    if w[i] <= a[i]:
        while s and s[-1] <= w[i]:
            res.append(s.pop())

        res.append(w[i])
    else:
        while s and s[-1] <= w[i] and s[-1] <= a[i]:
            res.append(s.pop())

        s.append(w[i])

while s:
    res.append(s.pop())

print(''.join(res))