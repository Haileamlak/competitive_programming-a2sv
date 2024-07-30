# Problem: C - Coffee Dilemma - https://codeforces.com/gym/528792/problem/C

from heapq import heappop, heappush

n = int(input())
a = list(map(int, input().split()))

curr = 0
heap = []

res = 0
for num in a:
    if num >= 0:
        curr += num
        res += 1
    else:
        curr += num
        heappush(heap, num)
        if curr < 0:
            curr -= heappop(heap)
        else:
            res += 1

print(res)