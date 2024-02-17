from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    index = [0 for _ in range(n)]
    for i in range(n):
        index[nums[i] - 1] += 1

    print(index)
    res = 0
    # for i in range()
    for i in range(2, n):

        temp = index[i] + index[i - 1] + index[i - 2]
        res += (temp * (temp - 1) * (temp - 2)) // 6

    print(res)