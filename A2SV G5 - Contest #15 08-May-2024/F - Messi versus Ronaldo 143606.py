# Problem: F - Messi versus Ronaldo - https://codeforces.com/gym/522079/problem/F

import sys
input = lambda: sys.stdin.readline().strip()

for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    count = [0] * 60

    for num in nums:
        i = 0
        while num:
            if 1 & num:
                count[i] += 1
            num >>= 1
            i += 1

    length = 60
    _mod = 1000_000_007

    res = 0
    for num in nums:
        _and = 0
        _or = 0
        for i in range(length):
            if (1 << i) & num:
                _and += (1 << i) * count[i]            
                _or += (1 << i) * n
            else:
                _or += (1 << i) * count[i]

        res += _and * _or 

    print(res % _mod)