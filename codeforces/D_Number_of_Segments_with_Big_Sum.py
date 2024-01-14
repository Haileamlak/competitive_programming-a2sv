n, s = map(int, input().split())

nums = list(map(int, input().split()))

left = 0
curr = 0
ans = 0
for right in range(n):
    curr += nums[right]
    while curr >= s:
        ans += n - right
        curr -= nums[left]
        left += 1


print(ans)