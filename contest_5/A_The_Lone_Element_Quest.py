for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    idx = 0
    num = 0
    if nums[1] != nums[0]:
        if nums[1] == nums[2]:
            print(1)
        else:
            print(2)
    else:
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                print(i + 1)
                break
            
