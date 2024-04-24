# Problem: D - Moving the Bishop - https://codeforces.com/gym/517685/problem/D

from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
start = list(map(int, input().split()))
target = list(map(int, input().split()))
target[0] -= 1
target[1] -= 1
start[0] -= 1
start[1] -= 1

target = tuple(target)

chess = []
for i in range(n):
    chess.append(input())

def inbound(r, c):
    return (0 <= r < n) and (0 <= c < n) and chess[r][c] == '.'

# def possible(x1, x2):
#     if x1 == x2:
#         return False

#     if (x1[0] * -1, x1[1] * -1) == x2:
#         return False
    
#     return True

directions = ((1, 1), (-1, -1), (-1, 1), (1, -1))

queue = deque([tuple(start)])
visited = [[0 for _ in range(n)] for _ in range(n)]

flag = False
res = 0

while queue:
    for _ in range(len(queue)):
        curr = queue.popleft()
        if curr == target:
            flag = True
            break
        
        visited[curr[0]][curr[1]] = 3
        for r, c in directions:
            nr, nc = curr[0] + r, curr[1] + c
            direction = r * c

            if not inbound(nr, nc) or ((direction == visited[nr][nc] or visited[nr][nc] == 3)):
                continue
            
            while inbound(nr, nc) :
                if not visited[nr][nc]:
                    visited[nr][nc] = direction
                    queue.append((nr, nc))
                else:
                    visited[nr][nc] = 3

                nr += r
                nc += c
            

    if flag:
        break

    res += 1

if flag:
    print(res)
else:
    print(-1)
