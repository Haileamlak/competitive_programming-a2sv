for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    
    nums.sort()

    if nums[0] != 1:
        print("NO")
        continue
    
    curr_sum = 1
    for i in range( 1,n):
        if curr_sum < nums[i]:
            print("NO")
            break
        curr_sum += nums[i]

    else:
        print("YES")