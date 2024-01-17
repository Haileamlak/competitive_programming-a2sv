t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    lsum = nums[0]
    rsum = 0
    left = 1
    right = n - 1
    res = 'NO'
    while left < right:
        lsum += nums[left]
        rsum += nums[right]
        if rsum > lsum:
            res = 'YES'
            break
        
        left += 1
        right -= 1
    
    print(res)