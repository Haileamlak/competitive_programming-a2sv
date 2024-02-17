k = int(input())
temp = [(0, {}) for _ in range(k)]
for j in range(k):
    n = int(input())
    nums = list(map(int, input().split()))
    dd = {}
    sm = 0
    for i in range(n):
        sm += nums[i]
        if nums[i] not in dd:
            dd[nums[i]] = i
    
    temp[j] = (sm, dd)

brek = False
for i in range(k):
    for j in range(i + 1, k):
        tt = temp[i]
        ff = temp[j]
        dec = ff[0] - tt[0]
        for t in tt[1]:
            if t + dec in ff[1]:
                print("YES")
                print(i + 1, tt[1][t] + 1)
                print(j + 1, ff[1][t + dec] + 1)
                brek = True
                break
        if brek:
            break
    if brek:
        break

else:
    print("NO")
