from math import ceil


t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    left = 0    
    right = n - 1

    x = 0
    res = 0
    while left < right:
        x += nums[left]

        if x >= nums[right]:
            res += nums[right] + 1
            x -= nums[right]
            right -= 1

        left += 1

    if left == right:
        x += nums[right]
        
    res += ceil(x / 2) + 1 if x > 1 else x
    print(res)