# Problem: C - Removal Hack - https://codeforces.com/gym/534160/problem/C

n = int(input())
tree = [[] for _ in range(n + 1)]
count = [0 for _ in range(n + 1)]
ct = [0 for _ in range(n + 1)]



for i in range(1, n + 1):
    p, c = map(int, input().split())
    
    if p != -1:
        tree[p].append(i)
        count[p] += 1 - c
    ct[i] = 1 - c

# print(tree)
# print(count)
# print(ct)
a = [i for i in range(1, n + 1) if count[i] == 0 and ct[i] == 0]
a.sort()
if len(a) == 0:
    print(-1)
else:
    print(*a)