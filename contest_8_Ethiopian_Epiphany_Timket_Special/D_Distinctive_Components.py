t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    res = 0
    for i in range(n):
        win = nums[0]
        l = 0
        for j in range(1, n):
            win += nums[j]


            while (win > nums[i]) and (j - l > 1):
                win -= nums[l]
                l += 1

            if win == nums[i]:
                res += 1
                break
            # if win == nums[i]:
            #     res += 1
            #     break
        # else:
        #     if win == nums[i]:
        #         res += 1

    print(res)