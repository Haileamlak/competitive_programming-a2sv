n = int(input())
nums = list(map(int, input().split()))

nums.sort()

i = 0
j = 1

while i < len(nums) and j < len(nums):
    while j < len(nums) and nums[j] <= nums[i]:
        j += 1

    if j < len(nums):
        i += 1
        j += 1

print(i)