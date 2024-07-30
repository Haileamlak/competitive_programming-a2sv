# Problem: E - Machine Testing - https://codeforces.com/gym/513152/problem/E

from math import ceil
for i  in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))

    stack = []
    res = 0

    for i in range(1, n):
        curr = 0
        while stack and h[i] > 0:
            if h[i] >= (stack[-1][0] * stack[-1][1]):
                h[i] -= (stack[-1][0] * stack[-1][1])
                curr += stack[-1][1]
                stack.pop()
            else:
                stack[-1][1] -= ceil(h[i] / stack[-1][0])
                curr += ceil(h[i] / stack[-1][0])
                h[i] = 0

        if h[i] > 0:
            x = ceil(h[i] / p[0]) 
            res += x
            curr += x

        stack.append([p[i], curr])
    
    print(res)