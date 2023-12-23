n = int(input())
problems = 0

for i in range(n):
    sure = list(map(int, input().split()))
    if sum(sure) >= 2:
        problems += 1

print(problems)
