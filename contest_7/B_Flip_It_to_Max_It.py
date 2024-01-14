t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    resSum = 0
    resOp = 0
    i = 0
    while i < len(nums):
        if nums[i] < 0:
            while i < len(nums) and nums[i] <= 0:
                resSum -= nums[i]
                i += 1
            
            resOp += 1

        # else:
        while i < len(nums) and nums[i] >= 0:
            resSum += nums[i]
            # resOp += 1
            i += 1 

    print(resSum, resOp)
