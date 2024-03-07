for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    nums = list(set(nums))
    nums.sort()

    res = 1

    end = 0
    for i in range(len(nums)):
        while end < len(nums) and nums[end] - nums[i] < n:
            end += 1
        
        res = max(res, end - i)
    
    print(res)