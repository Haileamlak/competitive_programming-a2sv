n = int(input())


# for _ in range(n):
nums = list(map(int, input().split()))

alex = nums[0]

# nums.sort(reverse=True)

res = 0
for i in range(1, len(nums)):
    if nums[i] < alex:
        res += 1

print(res)