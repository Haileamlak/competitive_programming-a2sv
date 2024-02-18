for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    x = 0
    val = sum(nums) // n

    for i in range(n - 1,-1,-1):
        if nums[i] <= val:
            x += (val - nums[i])
        else:
            x -= (nums[i] - val)
        
        if x < 0:
            print('NO')
            break
    else:
        print("YES")