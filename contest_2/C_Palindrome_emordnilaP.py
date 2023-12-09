t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    index = {}

    for i in range(n):
        if nums[i] in index:
            if i - index[nums[i]] >= 2:
                print("YES")
                break
        else:
            index[nums[i]] = i
    else:
        print("NO")
            