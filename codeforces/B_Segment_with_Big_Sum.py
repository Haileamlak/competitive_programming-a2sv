n, s = map(int, input().split())

nums = list(map(int, input().split()))

left = 0
curr = 0
ans = n + 1
for right in range(n):
    curr += nums[right]
    while curr >= s:
        ans = min(ans, right - left + 1)
        curr -= nums[left]
        left += 1


if ans == n + 1:
    print(-1)
else:
    print(ans)