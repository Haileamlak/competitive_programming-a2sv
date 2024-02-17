from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))    
    b = list(map(int, input().split()))
    # res = Counter(a + b)
    ca = {}
    cb = {}

    ccc = 1
    for i in range(1, n):
        if a[i] == a[i - 1]:
            ccc += 1
        else:
            t = 0
            if a[i - 1] in ca:
                t += ca[a[i - 1]]
            ca[a[i - 1]] = max(t, ccc)
            ccc = 1
    # ca [-1] = ccc
    
    t = 0
    if a[-1] in ca:
        t += ca[a[-1]]
    ca[a[-1]] = max(t, ccc)

    cc = 1
    for i in range(1, n):
        if b[i] == b[i - 1]:
            cc += 1
        else:
            t = 0
            if b[i - 1] in cb:
                t += cb[b[i - 1]]
            cb[b[i - 1]] = max(t, cc)
            cc = 1
    t = 0
    if b[-1] in cb:
        t += cb[b[-1]]
    cb[b[-1]] = max(t, cc)
    ans = 1
    for key, val in ca.items():
        temp = val
        if key in cb:
            temp += cb[key]
        
        ans = max(ans, temp)
    
    for key, val in cb.items():
        temp = val
        if key in ca:
            temp += ca[key]
        
        ans = max(ans, temp)

    # res = 1
    # ans = 1
    # i = 1
    # j = 0
    # tar = a[0]
    # while i < n or j < n:
    #     if i < n and tar == a[i]:
    #         i += 1
    #         res += 1
    #     elif j < n and tar == b[j]:
    #         j += 1
    #         res += 1
    #     else:
    #         ans = max(ans, res)
    #         res = 1
    #         if i < n:
    #             tar = a[i]
    #             i += 1
    #         else:
    #             tar = a[j]
    #             j += 1
    
    # ans = max(res, ans)
    # # while i < n:
        
    # #     if tar == a[i]:
    # #         i += 1
    # #         res += 1
    # #     else:
    # #         ans = max(ans, res)
    # #         res = 1
    # #         tar = a[i]
    # #         i += 1
    
    # while j < n:
        
    #     if tar == b[j]:
    #         j += 1
    #         res += 1
    #     else:
    #         ans = max(ans, res)
    #         res = 1
    #         tar = b[j]
    #         j += 1
    
    # ans =  max(res, ans)
    print(ans)