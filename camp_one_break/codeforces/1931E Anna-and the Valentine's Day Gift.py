for _ in range(int(input())):
    n, m = map(int, input().split())
    nums = input().split()


    nums.sort(key=lambda x : x[::-1])
    # print(nums)
    
    for i in range(0, n, 2):
        nums[i] = nums[i].rstrip('0')
    
    res = ''.join(nums)
    if len(res) - 1 < m:
        print('Anna')
    else:
        print('Sasha')