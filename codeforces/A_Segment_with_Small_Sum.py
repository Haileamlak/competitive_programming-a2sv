n, s = map(int, input().split())

nums = list(map(int, input().split()))

res = 0
curr = 0
left = 0
right = 0
while right < n:
    curr += nums[right]

    while curr > s:
        curr -= nums[left]
        left += 1

    res = max(res, right - left + 1)
    right += 1

print(res)