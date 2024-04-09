# Problem: F -  A Permutation Puzzle - https://codeforces.com/gym/515998/problem/F

from math import gcd


for i in range(int(input())):
    n = int(input())
    word = input()    
    per = list(map(int, input().split()))
    
    def shift(cycle):
        temp = cycle + cycle
        return temp[1:].find(cycle) + 1
    
    res = 1
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            cycle = ''
            while not visited[i]:
                visited[i] = True
                cycle += word[i]
                i = per[i] - 1
            
            x = shift(cycle)
            res = (res * x) // (gcd(res, x))

    print(res)