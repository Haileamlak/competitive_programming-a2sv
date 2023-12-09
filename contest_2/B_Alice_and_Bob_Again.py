t = int(input())

for _ in range(t):
    b = input()
    a = b[0]
    for i in range(1, len(b) - 1, 2):
        a += b[i]
    a += b[-1]
    print(a)
