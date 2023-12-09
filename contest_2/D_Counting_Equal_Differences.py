t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    freq = {}
    for i in range(n):
        diff = nums[i] - i
        freq[diff] = freq.get(diff, 0) + 1
    for val in freq.values():
        count += val * (val - 1) // 2
    print(count)
    