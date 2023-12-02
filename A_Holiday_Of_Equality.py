n = int(input())

burles = 0
mx = 0
nums = list(map(int, input().split()))
for i in range(len(nums)):
    if nums[i] > mx:
        burles += (nums[i] - mx) * i
        mx = nums[i]
    else:
        burles += (mx - nums[i])

print(burles)
