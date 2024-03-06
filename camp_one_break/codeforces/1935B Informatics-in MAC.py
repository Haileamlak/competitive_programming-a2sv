for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    bound = {}
    numset = set(nums)
    for i in range(n):
        if nums[i] not in bound:
            bound[nums[i]] = [i, i]
        else:
            bound[nums[i]][1] = i
    
    temp = [0, n - 1]
    for i in range(n):
        if i not in numset:
            print(2)
            print(1, temp[0] + 1)
            print(temp[0] + 2, n)
            break
        else:

            temp[0] = max(temp[0], bound[i][0])
            temp[1] = min(temp[1], bound[i][1])
            if temp[0] >= temp[1]:
                print(-1)
                break
    else:
        print(2)
        print(1, temp[0] + 1)
        print(temp[0] + 2, n)