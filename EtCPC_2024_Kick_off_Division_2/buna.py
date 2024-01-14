n = int(input())

nums = list(map(int, input().split()))

q = int(input())
for _ in range(q):
    i = int(input())
    print(nums[i - 1])