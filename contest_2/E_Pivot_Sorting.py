t = int(input())

from math import ceil
for j in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    num_set = set()
    x = [0, 10 ** 9]
    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i + 1]:
            x[0] = max(x[0], int(ceil((nums[i] + nums[i + 1]) / 2)))
        elif nums[i] < nums[i + 1]:
            x[1] = min(x[1], (nums[i] + nums[i + 1]) // 2)
    
    if x[0] <= x[1]:
        print(x[0])
    else:
        print(-1)