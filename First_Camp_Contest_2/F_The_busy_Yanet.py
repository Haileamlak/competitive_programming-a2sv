for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    idx = 0
    mn = nums[0]
    for i in range(1, n):
        if nums[i] < mn:
            mn = nums[i]
            idx = i

    for i in range(idx + 1, n):
        if nums[i] < nums[i - 1]:
            print(-1)
            break
    else:
        print(idx)