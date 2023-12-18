from math import ceil 
t = int(input())

for _ in range(t):
    n = int(input())
    
    if n % 2 == 0:
        print("NO")
    else:
        print("YES")
        half = ceil(n / 2)

        for i in range(1, half):
            print(i, i + half + n,)
        
        j = 1
        for i in range(half, n + 1):
            print(i, n + j )
            j += 1

