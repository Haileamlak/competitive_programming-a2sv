from collections import OrderedDict, Counter


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    possible = {}
    temp = Counter(nums)

    for i in temp:
        num = i
        res = -1
        left = -1
        for right in range(n):
            if nums[right] == num:
                res = max(res, right - left)
                left = right
        
        res = max(res, n - left)
        possible[i] = res

    # print(possible)

    lucky = [0 for _ in range(n)]
    for num in sorted(possible.keys()):
        # num = i 
        j = possible[num] - 1
        
        while j < n and lucky[j] == 0:
            lucky[j] = num
            j += 1
        
    i = 0
    while i < n and lucky[i] == 0:
        lucky[i] = -1
        i += 1
    
    print(*lucky)
            