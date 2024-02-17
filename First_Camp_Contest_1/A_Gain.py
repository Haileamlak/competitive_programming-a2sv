for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums2 = nums.copy()
    mx = max(nums)
    nums2.remove(mx)
    mx2 = max(nums2)
    for i in range(len(nums)):
        if nums[i] == mx:
            print(nums[i] - mx2, end=' ')
        else:
            print(nums[i] - mx, end=' ')
    
    print()
