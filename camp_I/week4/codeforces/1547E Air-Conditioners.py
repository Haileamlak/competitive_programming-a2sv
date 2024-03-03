for _ in range(int(input())):
    input()
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))

    c = [float('inf')] * n
    for i in range(k):
        c[a[i] - 1] = t[i]
    
    left = [0] * n
    right = [0] * n
    temp = float('inf')
    for i in range(n):
        temp = min(temp + 1, c[i])
        left[i] = temp
    
    temp = float('inf')
    for i in range(n - 1, -1, -1):
        temp = min(temp + 1, c[i])
        right[i] = temp

    for i in range(n):
        print(min(left[i], right[i]), end=' ')
    
    print()