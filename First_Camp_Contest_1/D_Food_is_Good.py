for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    simon = sum(nums)

    curr = 0
    aman = float('-inf')
    res = len(nums)
    l = 0
    for i in range(len(nums)):
        if nums[i] >= curr + nums[i]:
            curr = nums[i]
            l = i
        else:
            curr += nums[i]
        
        if curr == aman:
            res = min(res, i - l + 1)

        elif curr > aman:
            res = i - l + 1
            aman = curr
    
    if simon > aman:
        print("YES")
    else:
        if res < len(nums):
            print("NO")
        else:
            print("YES")
