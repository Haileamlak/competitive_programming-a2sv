# Problem: C - The Alchemist - https://codeforces.com/gym/530187/problem/C

import sys
from collections import defaultdict, deque
input = sys.stdin.readline
def solve():
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    nums = set(map(int, input().split()))

    graph = defaultdict(list)
    degree = [0] * (n + 1)
    future = [0] * (n + 1)
    ans = [0] * (n + 1)
    
    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        m, edges = line[0], line[1:]
        
        if i in nums:
            continue

        degree[i] = m
        for a in edges:
            graph[a].append(i)

    queue = deque()
    for node in range(1, n + 1):
        if node in nums:
            queue.append(node)
        elif degree[node] == 0:
            ans[node] = cost[node]
            queue.append(node)

    while queue:
        node = queue.popleft()
        for child in graph[node]:
            degree[child] -= 1
            future[child] += ans[node]
            if degree[child] == 0:
                queue.append(child)
                ans[child] = min(cost[child], future[child])

    print(*ans[1:])

q = int(input())
for _ in range(q):
    solve()


# import sys, threading

# input = lambda: sys.stdin.readline().strip()

# def main():
#     for i in range(int(input())):
#         n, k = map(int, input().split())
#         c = list(map(int, input().split()))
#         f = list(map(int, input().split()))
#         ff = set(f)
#         for i in f:
#             c[i - 1] = 0

#         a = [[] for _ in range(n)]
#         for i in range(n):
#             a[i] = (list(map(int, input().split()))[1:])

#         dp = [-1] * n
#         def foo(i):
#             if dp[i] != -1:
#                 return dp[i]
            
#             if len(a[i]) == 0:
#                 dp[i] = c[i]
#             else:
#                 dp[i] = min(c[i], sum([foo(j - 1) for j in a[i]]))

#             return dp[i]
        
#         for i in range(n):
#             print(foo(i), end=' ')

#         print()

# if __name__ == '__main__':
#     sys.setrecursionlimit(1 << 30)
#     threading.stack_size(1 << 27)

#     main_thread = threading.Thread(target=main)
#     main_thread.start()
#     main_thread.join()