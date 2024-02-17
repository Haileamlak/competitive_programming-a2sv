from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    # temp = Counter(b)
    # temp[10**9] = 1
    # bb = sorted(list(temp))
    b.append(10**9)
    b.sort(reverse=True)
    res = [0 for _ in range(n)]

    # i = 0
    c = 0
    # while i < len(b):
    for i in range(n):
        res[i] = b[c ]
        c += (i+1)

        # print(res[c])
        # c += 1
        # i += n - c 
        # res[c] = bb[i]
        # c += 1
        # if temp[b[i]] > n - c:
        #     for j in range(n - c, temp[b[i]]):
        #         res[c] = bb[i]
        #         c += 1
    
    print(* res)