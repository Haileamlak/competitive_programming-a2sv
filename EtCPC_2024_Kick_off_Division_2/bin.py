t = int(input())

for _ in range(t):
    n = input()
    res = 0
    one = False
    for i in range(len(n)):
        if (n[i] == '0' or n[i] == '1'):
            if not one:
                res += 1
            one = True
        else:
            res += 1

    print(res)