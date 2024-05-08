# Problem: C - ANDy Session - https://codeforces.com/gym/522079/problem/C

from collections import Counter


for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    count = Counter([])
    # count[0] = 0
    for num in nums:
        for i in range(num.bit_length()):
            if ((1 << i) & num) != 0:
                count[i] += 1
            
    # length = max(nums).bit_length()
   
    # x = max(length, 31 - (k // n))
    # res = ((1 << 31) - 1) - ((1 << x) - 1)
    
    # z = k % n
    # if (k // n) > 31 - x:
    #     z += (31 - (31 - (k // n))) - (31 - x)

    res = 0
    for i in range(30, -1, -1):
        if k >= (n - count[i]):
            
            k -= (n - count[i])
            res += 1 << i
    
    print(res)