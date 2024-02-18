for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    i = n - 1
    seen = set()
    while i >= 0:
        if nums[i] in seen:
            break
        seen.add(nums[i])
        i -= 1
    
    
    print(i + 1)