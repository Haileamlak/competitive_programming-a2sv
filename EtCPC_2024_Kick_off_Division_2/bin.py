t = int(input())

for _ in range(t):
    n = input()
    res = 1
    for i in range(len(n)):
        res = max(res, int(n[i]))

    print(res)