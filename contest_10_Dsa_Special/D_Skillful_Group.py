n = int(input())
nums = list(map(int, input().split()))
res  = 0

l = 0
temp = set()
r = n - 1
while l < n and nums[l] not in temp:
    temp.add(nums[l])
    l += 1

a = l

tempRight = set()
while r >= 0 and nums[r] not in tempRight:
    tempRight.add(nums[r])
    r -= 1


res = len(nums)
if l <= r:
    res = r - l + 1

# l = 0
# temp = set()
# r = n - 1

# while r >= 0 and nums[r] not in temp:
#     temp.add(nums[r])
#     r -= 1

# b = r
# while l < n and nums[l] not in temp:
#     temp.add(nums[l])
#     l += 1

# if l <= r:
#     res = min(res, r - l + 1)
    
#     res  = min(res, max(a, b) - min(a,b) + 1)
print(res)