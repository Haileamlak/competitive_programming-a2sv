n = int(input())
m = int(input())
nums = [0 for _ in range(n)]
for i in range(n):
    nums[i] = int(input())

nums.sort(reverse=True)

res = 0
reeee = 0
i = 0
while reeee < m:
    reeee += nums[i]
    res += 1
    i += 1

print(res)