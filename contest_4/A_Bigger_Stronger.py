t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    num_set = set()

    for i in range(n):
        if nums[i] in num_set:
            print("NO")
            break
        else:
            num_set.add(nums[i])
    else:
        print("YES")