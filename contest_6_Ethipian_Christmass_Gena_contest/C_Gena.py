n = int(input())
astu = list(map(int, input().split()))
m = int(input())
aau = list(map(int, input().split()))

astu.sort()
aau.sort()
i = 0
j = 0

res = 0 
while i < n and j < m:
    if abs(astu[i] - aau[j]) <= 1:
        res += 1
        i += 1
        j += 1
    elif astu[i] < aau[j]:
        i += 1
    else:
        j += 1

print(res)