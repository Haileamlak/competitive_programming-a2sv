# Problem: E - Blocking Paths for Safe Escape - https://codeforces.com/gym/515998/problem/E

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
import sys
input = lambda: sys.stdin.readline().strip()

for i in range(int(input())):
    n, m = map(int, input().split())
    maze = []
    goods = 0
    for i in range(n):
        row = input()
        goods += row.count('G')
        maze.append(row)
    
    def inbound(row, col):
        return (0 <= row < n) and (0 <= col < m)
    
    def wall(row, col):
        if maze[row][col] == '#':
            return True
        
        for i, j in directions:
            if inbound(row + i, col + j) and maze[row + i][col + j] == 'B':
                return True
        
        return False
    
    visited = [[False] * m for _ in range(n)]

    def dfs(row, col):
        if wall(row , col ):
            return 0

        good = 0
        
        stack = [(row, col)]
        visited[row][col] = True
        
        while stack:
            row, col = stack.pop()
            
            if maze[row][col] == 'G':
                good += 1
            
            for i, j in directions:
                if inbound(row + i, col + j) and not visited[row + i][col + j] and not wall(row + i, col + j):
                    stack.append((row + i, col + j))
                    visited[row + i][col + j] = True

        return good
    
    ans = dfs(n - 1, m - 1)
    
    if ans == goods:
        print('Yes')
    else:
        print('No')
