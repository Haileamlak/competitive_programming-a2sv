# Problem: C - Yet Another Monocarp's Problem - https://codeforces.com/gym/532814/problem/C

import sys


def solve():

    n, h = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))

    def checker(k):
        cur = k
        for i in range(n - 1):
            cur += min(k, a[i + 1] - a[i])
        return cur >= h
    
    low = 1
    high = h

    while low <= high:

        mid = (low + high)//2

        if checker(mid):
            high = mid - 1
        else:
            low = mid + 1
            
    return low
    
t = int(sys.stdin.readline().strip())  
for _ in range(t):
    print(solve())