n, q = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()
for i in range(1, n):
    nums[i] += nums[i - 1]

nums.insert(0, 0)
for _ in range(q):
    x, y = map(int, input().split())

    s = n - x
    
    res = (nums[s + y] - nums[s])
    print(res)