from collections import defaultdict
n, k = map(int, input().split())

nums = list(map(int, input().split()))

left = 0
window = defaultdict(int)
ans = 0
unique = 0
for right in range(n):
    if nums[right] not in window:
        unique += 1

    window[nums[right]] += 1

    while unique > k:
        window[nums[left]] -= 1
        if window[nums[left]] == 0:
            del window[nums[left]]
            unique -= 1
        left += 1
    
    ans += right - left + 1
    
print(ans)
