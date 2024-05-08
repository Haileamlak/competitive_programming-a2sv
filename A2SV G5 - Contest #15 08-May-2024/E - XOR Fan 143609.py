# Problem: E - XOR Fan - https://codeforces.com/gym/522079/problem/E

from functools import reduce


for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    s = input()

    def xor(x, y):
        return x ^ y
    
    ones = reduce(xor, [nums[i] for i in range(n) if s[i] == '1'] + [0])
    zeros = reduce(xor, [nums[i] for i in range(n) if s[i] == '0'] + [0])

    p = [0]
    for num in nums:
        p.append(num ^ p[-1])

    for i in range(int(input())):
        q = list(map(int, input().split()))
        if q[0] == 1:
            ones ^= p[q[2]] ^ p[q[1] - 1]
            zeros ^= p[q[2]] ^ p[q[1] - 1]
        else:
            if q[1] == 1:
                print(ones, end=' ')
            else:
                print(zeros, end=' ')
            
    print()