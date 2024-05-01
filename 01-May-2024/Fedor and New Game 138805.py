# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n, m, k = map(int, input().split())
players = []

for i in range(m + 1):
    players.append(int(input()))

def number_of_different(num1, num2):
    temp = num1 ^ num2
    count = 0
    while temp:
        temp &= temp - 1
        count += 1
    
    return count

res = 0
for i in range(m):
    if number_of_different(players[i], players[m]) <= k:
        res += 1

print(res)