from collections import defaultdict
n = int(input())

nums = list(map(int, input().split()))

temp = defaultdict(int)

for i in range(len(nums)):
    temp[nums[i] - i] += 1

res = 0
for val in temp.values():
    res += val * (val - 1) // 2

print(res * 2)
# for i in range(len(nums)):
#     for j in range(i, len(nums[]))