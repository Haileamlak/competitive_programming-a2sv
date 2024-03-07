for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    l = 1
    while l < len(nums) and nums[l] == nums[l - 1]:
        l += 1

    r = len(nums) - 2
    while r >= 0 and nums[r] == nums[r + 1]:
        r -= 1
    
    if nums[0] == nums[-1]:
        
        res = r - l + 1
    else:
        res = min(len(nums) - l, r + 1)
    if res > 0:
        print(res)
    else:
        print(0)