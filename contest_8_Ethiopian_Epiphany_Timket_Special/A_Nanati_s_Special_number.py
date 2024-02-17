t = int(input())

for _ in range(t):
    n = int(input())
    word = input()
    
    res = 97
    for l in word:
        res = max(res, ord(l))
    print(res - 96)