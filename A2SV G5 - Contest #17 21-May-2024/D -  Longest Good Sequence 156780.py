# Problem: D -  Longest Good Sequence - https://codeforces.com/gym/524965/problem/D

from collections import defaultdict

def prime_factors(n):
    factors = []
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p

        p += 1

    if n > 1:
        factors.append(n)
    
    return list(set(factors))

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()
    
dp = defaultdict(int)

for i in range(n):
    factors = prime_factors(a[i])
    res = 0
    for factor in factors:
        res = max(res, 1 + dp[factor])

    for factor in factors:
        dp[factor] = max(dp[factor], res)

    # for j in range(i + 1, n):
    #     if gcd(a[i], a[j]) > 1:
    #         dp[j] = max(dp[j], dp[i] + 1)
            # break
# print(dp)
print(max(dp.values()))