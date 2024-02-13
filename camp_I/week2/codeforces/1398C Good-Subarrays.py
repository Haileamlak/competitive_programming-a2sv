import collections

for _ in range(int(input())):
    n = int(input())
    given = input()
    arr = [int(given[i] ) for i in range(len(given))]

    pre_map = collections.defaultdict(int)
    pre_map[0] = 1

    currSum = 0
    res = 0
    for i in range(len(arr)):
        currSum += arr[i]

        x = currSum - i - 1
        pre_map[x] += 1
        res += pre_map[x] - 1

    # for key, value in pre_map.items():
    #     n = value
    #     res += n * (n - 1) // 2

    print(res)