for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    x = max(nums)
    y = min(nums)
    # res = 0
    # for num in nums:
    #     res += (x - num)
    
    print(x - y)