# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

class MyTuple:
    def __init__(self, _tuple):
        self._tuple = _tuple

    def __lt__(self, other):
        return self._tuple[0] < other[0]

    def __getitem__(self, index):
        return self._tuple[index]

from heapq import heapify, heappop, heappush


for _ in range(int(input())):
    n = int(input())
    social = list(map(int, input().split()))
    social = [MyTuple((-num, i + 1)) for i, num in enumerate(social) if num > 0]
    heapify(social)
    res = []
    while len(social) > 1:
        person1, person2 = heappop(social), heappop(social)
        res.append((person1[1], person2[1]))

        if person1[0] < -1:
            heappush(social, MyTuple((person1[0] + 1, person1[1])))

        if person2[0] < -1:
            heappush(social, MyTuple((person2[0] + 1, person2[1])))
    
    print(len(res))
    for x1, x2 in res:
        print(x1, x2)