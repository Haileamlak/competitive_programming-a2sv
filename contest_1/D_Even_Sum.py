n = int(input())

min = 10**9 + 1
sum = 0
nums = list(map(int, input().split()))

for i in range(n):
    sum += nums[i]
    if nums[i] % 2 != 0 and nums[i] < min:
        min = nums[i]

if sum % 2 != 0:
    print(sum - min)
else:
    print(sum)

# print(10**9)