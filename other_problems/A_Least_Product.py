t = int(input())

for _ in range(t):
    n = int(input())

    nums = list(map(int, input().split()))
    nums.sort()

    if nums[0] == 0:
        print(0)
    elif nums[0] > 0:
        print(1)
        print(1, 0)
    else:
        i = 0
        while i < n and nums[i] < 0:
            i += 1
        
        if i < n and nums[i] == 0:
            print(0)
        elif i % 2 == 0:
            print(1)
            print(1, 0)
        else:
            print(0)