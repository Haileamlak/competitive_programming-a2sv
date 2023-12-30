for _ in range(int(input())):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    if n > m:
        print("NO")
    else:
        chairs = 1 + nums[0] * 2
        # chairs += (nums[0] * 2) + 1
        for i in range(1, n - 1):
            chairs += 1 + nums[i] + (nums[i] - nums[i - 1])

        chairs += 1 + (nums[-1] - nums[-2]) + (nums[-1] - nums[0])
        if chairs > m:
            print("NO")
        else:
            print("YES")