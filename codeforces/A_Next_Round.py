n, k = map(int, input().split())

scores = list(map(int, input().split()))


i = 0

while i < n and scores[i] >= scores[k - 1] and scores[i] != 0:
    i += 1

print(i)