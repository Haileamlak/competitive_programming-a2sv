t = int(input())

for _ in range(t):
    n = int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    nums1 = [[a, b] for a, b in zip(alice, bob)]
    nums2 = [[a, b] for a, b in zip(alice, bob)]

    nums1.sort(key=lambda num:num[0])
    nums2.sort(key=lambda num:num[1], reverse=True)

    # print(nums)
    i = 0
    j = n - 1
    isALice = True
    res = 0
    while i <= j:
        if isALice:
            res += nums1[j][0] - 1
            isALice = False
            j -= 1
        else:
            res -= nums2[i][1] - 1
            i += 1
            isALice = True
    
    print(res)