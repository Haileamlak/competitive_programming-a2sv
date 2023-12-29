t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))

    if nums[0] == nums[1]:
        print(nums[2])
    elif nums[1] == nums[2]:
        print(nums[0])
    else:
        print(nums[1])