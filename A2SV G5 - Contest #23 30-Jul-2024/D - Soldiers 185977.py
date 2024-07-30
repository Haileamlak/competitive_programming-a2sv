# Problem: D - Soldiers - https://codeforces.com/gym/532814/problem/D

import sys

input = sys.stdin.readline
dp = [0] * 5000005

def solve():
    n, m = map(int, input().split())
    print(dp[n] - dp[m])

def sieve(n):
    primes = [True] * (n + 1)
    for i in range(2, n + 1):
        if not primes[i]:
            continue
        num = i * 2
        while num <= n:
            primes[num] = False
            num += i

    ans = [i for i in range(2, n + 1) if primes[i]]
    return ans

def preCompute():

    
    ans = sieve(5000001)
    for a in ans:
        dp[a] = 1

    q = int(input())

    for i in range(2, 5000001):
        if dp[i]:
            continue
        d = 0
        while ans[d] * ans[d] <= i:
            if i % ans[d] == 0:
                dp[i] = dp[i // ans[d]] + 1
                break
            d += 1

    for i in range(1, 5000001):
        dp[i] += dp[i - 1]

    for i in range(q):
        solve()

if __name__ == "__main__":
    preCompute()