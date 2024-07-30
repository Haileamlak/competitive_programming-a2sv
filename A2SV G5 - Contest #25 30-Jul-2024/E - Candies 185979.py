# Problem: E - Candies - https://codeforces.com/gym/535749/problem/E


MAX = 10 ** 5 + 1
MOD = 10 ** 9 + 7
t, k = map(int, input().split())

# it is obvious that the number of ways to in which Marmont can eat his dinner is 1 if the number of candies is less than k 
prfx = [1] * MAX
prfx[0] = 0

# if the number of candies is equal to k the number of ways to eat his dinner is 2
prfx[k] = 2

# if the number of candies is greater than k the number of ways to eat his dinner is prfx[ith - 1] + prfx[ith - k] 
for i in range(k + 1, MAX):
    prfx[i] = (prfx[i - 1] + prfx[i - k]) % MOD 

# calculating the prefix sum of the number of ways to eat his dinner to minimize the time complexity from O(t * (b - a)) to O(MAX)
for i in range(1, MAX):
    prfx[i] = (prfx[i] + prfx[i - 1]) % MOD

for _ in range(t):
    a, b = map(int, input().split())
    print((prfx[b] - prfx[a - 1]) % (10 ** 9 + 7))