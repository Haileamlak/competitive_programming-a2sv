from math import ceil
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = [(0, 0) for _ in range(n)]
    for i in range(n):
        ab[i] = (a[i], b[i])
    
    ab.sort(reverse=True, key= lambda x:(x[0] + x[1]))
    
    ans = 0
    for i in range(0, n, 2):
        
        ans += (ab[i][0] - 1)
    
    for i in range(1, n, 2):
        ans -= (ab[i][1] - 1)
    

    print(ans)