t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    f = input()
    add = 0
    rem = 0

    for i in range(n):
        if s[i] != f[i]:
            if s[i] == '0':
                add += 1
            else:
                rem += 1
            
    print(max(add, rem))